from langchain_core.prompts import ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手, 我的的名字是{username}, 你可以回答用户的问题, 你可以使用中文和英文进行交流. "),
])

human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])

chat_prompt = system_chat_prompt + human_chat_prompt

print(chat_prompt.invoke({
    "username": "llmops",
    "query": "你好, 你是？"
}))