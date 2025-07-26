from typing import Any

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from wtforms.validators import AnyOf

dotenv.load_dotenv()

# 1.构建组件
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)
parser = StrOutputParser()

# 2.定义一个链类，用于串联多个组件
class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        """执行链中的每个步骤"""
        for step in self.steps:
            input = step.invoke(input)
            print("步骤", step)
            print("输出", input)
            print("=================")
        return input

# 3.编排链
chain = Chain([prompt, llm, parser])

# 4.执行链并获取结果
print(chain.invoke({"query": "你好你是？"}))