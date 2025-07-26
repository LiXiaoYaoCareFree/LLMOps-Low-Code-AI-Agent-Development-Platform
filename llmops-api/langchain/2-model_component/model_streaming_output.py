from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant.Time is {now}."),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

response = llm.stream(prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}))

for chunk in response:
    print(chunk.content,flush=True,end="")