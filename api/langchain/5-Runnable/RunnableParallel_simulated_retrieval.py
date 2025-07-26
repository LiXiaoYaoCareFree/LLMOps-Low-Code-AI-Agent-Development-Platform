import dotenv
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

def retrieve(query: str) -> str:
    """
    模拟检索上下文的函数
    """
    print("正在检索与查询相关的上下文...")
    return "我是lly"


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文生成

<context>
{context}
</context>

用户的提问是: {query}""")

# 2.构建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.构建链
chain = RunnableParallel({
    "context": lambda x: retrieve(x["query"]),
    "query": itemgetter("query"),
}) | prompt | llm | parser

# 4.调用链
content = chain.invoke({"query": "你好，我是谁？"})

print(content)