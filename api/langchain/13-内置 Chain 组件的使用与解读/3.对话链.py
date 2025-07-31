import dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(model="kimi-k2-0711-preview")
chain = ConversationChain(llm=llm)

content = chain.invoke({"input": "你好，我是lly，我喜欢打篮球还有游泳，你喜欢什么运动呢？"})

print(content)

content = chain.invoke({"input": "根据上下文信息，请统计一下我的运动爱好有什么?"})

print(content)
