import dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

# 1.编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话,尽可能短一些\n")
poem_prompt = ChatPromptTemplate.from_template("请写一首关于{subject}的诗,尽可能短一些\n")


# 2.构建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.调用模型并解析输出
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.并行链
map_chain = RunnableParallel({
    "joke": joke_chain,
    "poem": poem_chain
})

res = map_chain.invoke({"subject": "程序员"})

print(res)