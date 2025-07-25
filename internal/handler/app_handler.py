import uuid

from injector import inject
from dataclasses import dataclass
import os
import dotenv

from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json, success_message
from internal.exception import FailException
from internal.service import AppService
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

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入，GET?POST?
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")

        # 2.构建Openai客户端，并发起请求
        llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        ai_message = llm.invoke(prompt.invoke({"query": req.query}))

        parser = StrOutputParser()

        # 4.解析响应内容
        content = parser.invoke(ai_message)

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}

