from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    )

from datetime import datetime
from langchain_core.messages import AIMessage

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt.format(subject="程序员"))
prompt_value = (prompt.invoke({"subject": "程序员"}))
print(prompt_value.to_string())
print(prompt_value.to_messages())


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的输入回答问题，当前的时间为：{now}"),
    # 有时候可能还有其他的消息，但是不确定
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话"),
]).partial(now=datetime.now())

chat_prompt_value = chat_prompt.invoke({
    "subject": "程序员",
    "chat_history": [
        {"role": "user", "content": "你好"},
        AIMessage(content="你好，我是Kimi开发的聊天机器人。")
    ]

})
print(chat_prompt_value)
print(chat_prompt_value.to_string())