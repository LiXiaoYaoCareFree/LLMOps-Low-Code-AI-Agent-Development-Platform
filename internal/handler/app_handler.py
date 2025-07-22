import os

from flask import request
from openai import OpenAI
from flask import jsonify
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json
from internal.exception import FailException

class AppHandler:
    """应用控制器"""
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

