"""
LLM与ChatModel是在自然语言处理（NLP）领域两种常见的人工智能模型。
一、LLM（纯文本补全模型）
LLM是一类设计用来生成或补全文本的模型。它们通常基于变换器（Transformer）架构，能够处理大规模数据集，并生成连贯、语法正确的文本。

LLM输入输出
输入：LLM可以接受一段文本作为输入，这段文本可以是一个句子、一个段落，甚至是一整篇文章的开始部分。
输出：模型基于输入文本生成续写或补全的文本。
数学公式：在数学上，可以表示为：
Output=LLM(Input)\text{Output} = \text{LLM}(\text{Input})Output=LLM(Input)
其中，Input是用户提供的文本，Output是模型生成的文本续写。

示例说明
假设我们有一个LLM，我们给它输入一段文本：
输入：今天天气真好，我打算去公园散步。
输出：顺便还可以看看公园里的花都开了没有。
在这个例子中，LLM根据给定的句子生成了一个合理的续写。

二、ChatModel（聊天模型）
ChatModel是专门为对话系统设计的模型，它们不仅生成文本，还能在多轮对话中保持上下文连贯性。
ChatModel输入输出
输入：ChatModel的输入通常包括用户的消息和之前对话的上下文。
输出：模型生成的回复需要与之前的对话内容相关联，保持话题的连贯性。
数学公式：在数学上，ChatModel的输入输出关系可以表示为：
Reply=ChatModel(UserMessage,Context)\text{Reply} = \text{ChatModel}(\text{UserMessage}, \text{Context})Reply=ChatModel(UserMessage,Context)
其中，UserMessage是用户的消息，Context是对话上下文，Reply是模型生成的回复。

示例说明
假设我们有一个ChatModel，并且已经进行了以下对话：
用户：今天天气真好，我打算去公园散步。
模型：听起来是个不错的计划！你打算去哪个公园？

用户回复：
输入：我打算去中央公园。
输出：中央公园是个不错的选择，那里有很多美丽的景点和活动。

在这个例子中，ChatModel根据用户的回答和之前的对话上下文生成了一个相关的回复。

结论
LLM和ChatModel各有其优势和适用场景。LLM擅长文本生成和补全，而ChatModel则更擅长处理交互式的对话。在选择使用哪种模型时，需要根据具体任务的需求来决定。无论是创作文章、编写代码，还是构建客户服务聊天机器人，这两种模型都能在不同的应用中发挥重要作用。
"""

"""
对话模板，用于ChatModel的提示词
"""

def chat_prompt_template_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_dev1 enter\n")
    template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    formatted1 = template.format(role="翻译助手", user_input="帮我翻译下面这段文字")
    formatted2 = template.format_messages(role="翻译助手", user_input="帮我翻译下面这段文字")
    print("type(formatted): " + str(type(formatted1)))
    print(formatted1)

    print("="*20)
    print("type(formatted2): " + str(type(formatted2)))
    print(formatted2)
    print("\nchat_prompt_template_dev1 exit")

def chat_prompt_template_dev2():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import SystemMessage
    from langchain_core.messages import HumanMessage
    from langchain_core.messages import AIMessage
    # 更灵活的组装
    system_msg = SystemMessage(
        content="你是一个翻译助手",
        additional_kwargs={"语言": "中文、英文、日语、法语"}
    )
    human_msg = HumanMessage(content="帮我翻译下面这段文字")
    ai_msg = AIMessage(content="好的，请提供需要翻译的文本。")
    chat_msgs = [system_msg, human_msg, ai_msg]
    print("type(chat_msgs): " + str(type(chat_msgs)))
    print("chat_msgs:" + str(chat_msgs))

    chat_prompt_template = ChatPromptTemplate.from_messages(chat_msgs)
    print("chat_prompt_template:" + str(chat_prompt_template))


def chat_message_prompt_template_dev1():
    from langchain_core.prompts import SystemMessagePromptTemplate
    from langchain_core.prompts import HumanMessagePromptTemplate
    from langchain_core.prompts import AIMessagePromptTemplate
    from langchain_core.prompts import ChatMessagePromptTemplate


    prompt_template = "帮我解释一下{topic}"
    system_msg_prompt = SystemMessagePromptTemplate.from_template(template=prompt_template)
    prompt_format_msg = system_msg_prompt.format(topic="Transformer模型")
    print("type(system_msg_prompt): " + str(type(system_msg_prompt)))
    print("system_msg_prompt:" + str(system_msg_prompt))
    print("prompt_format_msg:" + str(prompt_format_msg))

    print("="*20)
    human_msg_prompt = HumanMessagePromptTemplate.from_template(template=prompt_template)
    prompt_format_msg = human_msg_prompt.format(topic="Transformer模型")
    print("type(human_msg_prompt): " + str(type(human_msg_prompt)))
    print("human_msg_prompt:" + str(human_msg_prompt))
    print("prompt_format_msg:" + str(prompt_format_msg))

    print("="*20)
    ai_msg_prompt = AIMessagePromptTemplate.from_template(template=prompt_template)
    prompt_format_msg = ai_msg_prompt.format(topic="Transformer模型")
    print("type(ai_msg_prompt): " + str(type(ai_msg_prompt)))
    print("ai_msg_prompt:" + str(ai_msg_prompt))
    print("prompt_format_msg:" + str(prompt_format_msg))

    print("="*20)
    chat_msg_prompt = ChatMessagePromptTemplate.from_template(template=prompt_template, role="user_h")
    prompt_format_msg = chat_msg_prompt.format(topic="Transformer模型")
    print("type(chat_msg_prompt): " + str(type(chat_msg_prompt)))
    print("chat_msg_prompt:" + str(chat_msg_prompt))
    print("prompt_format_msg:" + str(prompt_format_msg))

def main():
    # chat_prompt_template_dev1()
    # chat_prompt_template_dev2()
    chat_message_prompt_template_dev1()


if __name__ == '__main__':
    main()