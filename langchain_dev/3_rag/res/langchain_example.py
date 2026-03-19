# 推荐使用 ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chat_model = ChatOpenAI(model="gpt-4o-mini")
messages = [HumanMessage(content="你好！")]
response = chat_model.invoke(messages)

# 不推荐使用 OpenAI（仅用于兼容旧代码）
from langchain_openai import OpenAI

llm = OpenAI(model="text-davinci-003")  # 已废弃
response = llm.invoke("你好！")