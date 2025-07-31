import uuid
from dataclasses import dataclass
from operator import itemgetter
from uuid import UUID
import os

from injector import inject
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from api.internal.exception import FailException
from api.internal.schema.app_schema import CompletionReq
from api.internal.service import AppService
from api.pkg.response import success_json, validate_error_json, success_message
from api.internal.exception import FailException
from api.internal.service import AppService
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

api_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
storage_path = os.path.join(api_dir, 'storage', 'memory', 'chat_history.txt')

@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        """根据ID获取应用"""
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为:{app.id}")

    def debug(self, app_id: UUID):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.创建prompt与记忆
        prompt = ChatPromptTemplate.from_messages([
            ("system", "你是一个强大的聊天机器人，能根据用户的提问回复对应的问题"),
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])
        memory = ConversationBufferWindowMemory(
            k=3,
            input_key="query",
            output_key="output",
            return_messages=True,
            chat_memory=FileChatMessageHistory(storage_path),
        )

        # 3.创建llm
        llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7, max_tokens=1000)

        # 4.创建链应用
        chain = RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        ) | prompt | llm | StrOutputParser()

        # 5.调用链生成内容
        chain_input = {"query": req.query.data}
        content = chain.invoke(chain_input)
        memory.save_context(chain_input, {"output": content})

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}

