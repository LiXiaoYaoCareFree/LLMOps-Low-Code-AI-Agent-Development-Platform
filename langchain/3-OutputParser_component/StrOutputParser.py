from langchain_core.output_parsers import StrOutputParser
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 2.构建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.调用模型并解析输出
content = parser.invoke(llm.invoke(prompt.invoke({"query": "请给我讲一个关于人工智能的笑话"})))

print(content)  # 输出解析后的字符串内容