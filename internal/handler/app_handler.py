import uuid

from injector import inject
from dataclasses import dataclass
import os

from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json, success_message
from internal.exception import FailException
from internal.service import AppService

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

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入，GET?POST?
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        query = request.json.get("query")

        # 2.构建Openai客户端，并发起请求
        client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))

        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model="kimi-k2-0711-preview",
            messages=[{"role": "system", "content": "你是一个AI助手，根据用户的输入回答相应的问题"},
                      {"role":"user", "content": query},
            ]
        )

        content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}

