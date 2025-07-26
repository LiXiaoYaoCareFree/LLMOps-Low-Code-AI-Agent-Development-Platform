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

# 2.创建链
chain = prompt | llm | parser

# 3.调用invoke方法
print(chain.invoke({"query":"请给我讲一个关于人工智能的笑话"}))