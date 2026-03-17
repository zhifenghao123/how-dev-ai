"""
在 LangChain 中，‌ChatOpenAI 和 OpenAI 是两个用于调用 OpenAI 模型的不同类，核心区别在于‌模型类型、输入输出格式、适用场景和功能支持‌。
1. 核心区别概览‌
（1）OpenAI
调用的是 ‌文本补全（Text Completion）模型‌，如 text-davinci-003（已废弃）或嵌入模型（如 text-embedding-ada-002）。
使用 /v1/completions 接口。
输入为‌纯字符串‌，输出为‌字符串‌。
‌不支持多轮对话、工具调用、JSON 模式等现代功能‌。
当前状态：‌已标记为 Legacy（遗留）‌，‌不推荐用于新项目‌

（2）ChatOpenAI
调用的是 ‌聊天（Chat Completion）模型‌，如 gpt-3.5-turbo、gpt-4o、gpt-4o-mini。
使用 /v1/chat/completions 接口。
输入为‌消息列表‌（如 [SystemMessage(), HumanMessage()]），输出为‌结构化 AIMessage 对象‌。
‌支持多轮对话、工具调用、JSON 模式、流式输出、上下文管理‌等现代 LLM 功能。
当前状态：‌LangChain 中与 OpenAI 交互的首选类‌，兼容最新模型和生态

2. 适用场景建议‌
（1）‌使用 ChatOpenAI 当‌：
构建聊天机器人、虚拟助手、客服系统。
需要多轮对话、记忆上下文（结合 RunnableWithMessageHistory）。
要求结构化输出（如 JSON）或调用外部工具（Agent 场景）。
使用 LangChain 表达式语言（LCEL）或 LangGraph。
（2）‌使用 OpenAI 仅当‌：
兼容旧代码（如使用 text-davinci-003）。
调用嵌入模型（如 text-embedding-ada-002）进行向量化。

3. 性能与成本‌
ChatOpenAI 支持最新模型（如 gpt-4o-mini），‌性价比高、延迟低、性能强‌，适合大规模部署
OpenAI 依赖已废弃模型，‌成本高、性能差、无更新支持‌，应避免使用

总结‌
✅ ‌新项目一律使用 ChatOpenAI‌；
❌ ‌避免使用 OpenAI 类调用 GPT 系列对话模型‌。
"""

import os

from dotenv import load_dotenv
from langchain_openai import OpenAI


def llm_call():
    # 优先使用环境变量中的配置
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('OPENAI_API_KEY', '')
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo-instruct')

    print(f"base_url: {base_url}, api_key: {api_key}, model: {model}")
    # 检查API密钥是否为空
    if not api_key:
        print("❌ API密钥为空，请设置 OPENAI_API_KEY 环境变量")
        return

    try:
        # 创建一个OpenAI实例（传统completion API）
        llm = OpenAI(base_url=base_url, api_key=api_key, model=model)

        # 使用直接字符串调用（传统completion API方式）
        response = llm.invoke("你好")
        print(f"✅ AI回复: {response}")
    except Exception as e:
        print(f"❌ 调用失败: {e}")


def main():
    # Load environment variables from .env file
    load_dotenv()

    llm_call()


if __name__ == '__main__':
    main()