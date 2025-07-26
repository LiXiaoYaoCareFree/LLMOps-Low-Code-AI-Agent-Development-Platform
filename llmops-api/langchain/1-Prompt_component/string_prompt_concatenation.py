from langchain_core.prompts import PromptTemplate


prompt = (
    PromptTemplate.from_template("请将一个关于{subject}的冷笑话")
    + "，让我笑一笑。" +
    "\n使用{language}语言回答。"
)



print(prompt.invoke({"subject": "Python", "language": "中文"}).to_string())
