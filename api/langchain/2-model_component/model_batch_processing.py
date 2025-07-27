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

ai_messages = llm.batch([
    prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}),
    prompt.invoke({"query": "请给我讲一个关于人工智能的笑话"}),
    prompt.invoke({"query": "你能告诉我今天的天气吗？"}),
])


for ai_message in ai_messages:
    print(ai_message.content)
    print("-" * 40)  # 分隔符