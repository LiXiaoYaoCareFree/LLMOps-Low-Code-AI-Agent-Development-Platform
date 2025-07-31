import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])
llm = ChatOpenAI(model="gpt-3.5-turbo")

chain = prompt | llm.bind(model="gpt-4o") | StrOutputParser()

content = chain.invoke({"query": "你是什么模型呢？"})

print(content)
