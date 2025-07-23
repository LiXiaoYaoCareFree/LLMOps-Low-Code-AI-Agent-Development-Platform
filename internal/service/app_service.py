from injector import inject
from pkg.sqlalchemy import SQLAlchemy
import uuid
from dataclasses import dataclass

from internal.model import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit():
            # 1.创建模型的实体类
            app = App(name="测试机器人", account_id = uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
            # 2.将实体类添加到session会话中
            self.db.session.add(app)
        return app

    def get_app(self, id: uuid.UUID) -> App:
        """根据ID获取应用"""
        app = self.db.session.query(App).get(id)
        if not app:
            raise ValueError(f"应用ID {id} 不存在")
        return app


    def update_app(self, id: uuid.UUID) -> App:
        """更新应用"""
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "更新后的应用名称"
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        """删除应用"""
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app