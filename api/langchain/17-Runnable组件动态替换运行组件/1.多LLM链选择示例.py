import dotenv
from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.创建提示模板&定义默认大语言模型
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="kimi-k2-0711-preview").configurable_alternatives(
    ConfigurableField(id="llm"),
    default_key="kimi-k2-0711-preview",
    gpt4=ChatOpenAI(model="kimi-k2-0711-preview"),
    wenxin=QianfanChatEndpoint(),
)

# 2.构建链应用
chain = prompt | llm | StrOutputParser()

# 3.调用链并传递配置信息，并切换到文心一言模型或者gpt4模型
content = chain.invoke(
    {"query": "你好，你是什么模型呢?"},
    config={"configurable": {"llm": "kimi-k2-0711-preview"}}
)
print(content)
