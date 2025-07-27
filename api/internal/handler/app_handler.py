import uuid
from uuid import UUID
from injector import inject
from dataclasses import dataclass
import dotenv

from api.internal.schema.app_schema import CompletionReq
from api.pkg.response import success_json, validate_error_json, success_message
from api.internal.exception import FailException
from api.internal.service import AppService
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经创建成功，应用ID为{app.id}")

    def get_app(self, id: uuid.UUID):
        """根据ID获取应用"""
        app = self.app_service.get_app(id)
        return success_json(f"应用已经成功获取，应用名称为{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功更新，修改的名字为{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，应用名称为{app.name}")

    def debug(self, app_id: UUID):
        """聊天接口"""
        # 1.提取从接口中获取的输入，GET?POST?
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)
        parser = StrOutputParser()

        # 3.构建链
        chain = prompt | llm | parser

        # 4.执行链并获取结果
        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}

