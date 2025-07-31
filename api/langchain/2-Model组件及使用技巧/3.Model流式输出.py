from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview")

response = llm.stream(prompt.invoke({"query": "你能简单介绍下LLM和LLMOps吗?"}))

for chunk in response:
    print(chunk.content, flush=True, end="")
