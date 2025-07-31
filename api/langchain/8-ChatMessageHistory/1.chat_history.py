
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("你好，我是lly，你是谁？")
chat_history.add_ai_message("你好，我是ChatGPT，有什么可以帮到您的？")

print(chat_history.messages)
