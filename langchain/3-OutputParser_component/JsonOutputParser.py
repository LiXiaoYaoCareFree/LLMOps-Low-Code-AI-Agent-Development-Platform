import dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.创建一个json数据结构，用于告诉大语言模型这个json长什么样子
class Joke(BaseModel):
    """笑话数据模型"""
    # 冷笑话
    joke: str = Field(description="回答用户的冷笑话")
    # 冷笑话的笑点
    punchline: str = Field(description="冷笑话的笑点")

parser = JsonOutputParser(pydantic_object=Joke)

# 2.构建一个提示模板
prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instructions}\n\n用户提问：{query}").partial(
    format_instructions=parser.get_format_instructions())

# 3.创建大语言模型
llm = ChatOpenAI(model="kimi-k2-0711-preview", temperature=0.7)

# 4.调用大语言模型
joke = parser.invoke(llm.invoke(prompt.invoke({"query": "请给我讲一个关于Python的冷笑话"})))

print(type(joke))
print(joke.get("punchline"))
print(joke)