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

"""
1、ChatPromptTemplate如何获取实例
（1）使用构造方法的方式
（2）使用from_messages()方法【推荐】
"""
def prompt_template_instance_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    chat_rompt_template = ChatPromptTemplate(
        messages=[
            ("system", "你是一个{role}"),
            ("human", "请帮我{task}"),
        ],
        # input_variables=["role", "task"] # 也可省略，能自动识别出来
    )
    print(chat_rompt_template)
    print(type(chat_rompt_template))
    print(chat_rompt_template.format(role="翻译助手", task="翻译这段文字"))

def prompt_template_instance_dev2():
    from langchain_core.prompts import ChatPromptTemplate
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "请帮我{task}"),
        ]
    )
    print(chat_rompt_template)
    print(type(chat_rompt_template))
    print(chat_rompt_template.format(role="翻译助手", task="翻译这段文字"))


"""
2、给变量赋值的两种方式（调用提示词模板的方式）
（1）invoke()：参数为包含各个变量键值对的字典，返回的是ChatPromptValue对象
（2）format()：参数为各个变量，返回的是str
（3）format_messages()：参数为各个变量，返回的是ChatMessage对象列表
（4）format_prompt()：参数为各个变量，返回的是ChatPromptValue对象

如何实现ChatPromptValue对象、list[ChatMessage]、str之间的转换？

"""

def chat_prompt_template_invoke_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_invoke_dev1 enter\n")
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_rompt_template.invoke({"role": "翻译助手", "user_input": "帮我翻译下面这段文字"})
    print(result)
    print(type(result))


def chat_prompt_template_format_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_format_dev1 enter\n")
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_rompt_template.format(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))

def chat_prompt_template_format_messages_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_format_messages_dev1 enter\n")
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_rompt_template.format_messages(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))

def chat_prompt_template_format_prompt_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_format_prompt_dev1 enter\n")
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_rompt_template.format_prompt(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))

def chat_prompt_template_result_convert_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_result_convert_dev1 enter\n")
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_rompt_template.format_prompt(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))

    # ChatPromptValue对象转换为list[ChatMessage]
    print("ChatPromptValue convert to messages" +"="*20)
    result_to_messages = result.to_messages()
    print(result_to_messages)
    print(type(result_to_messages))

    # ChatPromptValue对象转换为str
    print("ChatPromptValue convert to str" + "=" * 20)
    result_to_str = result.to_string()
    print(result_to_str)
    print(type(result_to_str))

"""
3、更丰富的实例化参数形式
本质：不管使用构造方法、还是使用from_message(）来创建ChatPromptTemplate的实例，本质上来讲，传入的都是消息构成的列表。
从调用上来讲，我们看到，不管使用构造方法，还是使用from_message(），messages参数的类型都是列表，但是列表的元素的类型是多样的。元素可以是：
字符串类型、字典类型、消息类型、元组构成的列表（最常用、最基础、最简单）、Chat提示词模板类型、消息提示词模板类型

"""
def chat_prompt_template_parameter_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_parameter_dev1 enter\n")
    # 字符串类型
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            "我的问题是：{question}"  # 字符串类型,默认的角色是human
        ]
    )
    result = chat_rompt_template.format_prompt(question="什么是Transformer模型？")
    print(result)
    print(type(result))

def chat_prompt_template_parameter_dev2():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_parameter_dev2 enter\n")
    # 字典类型
    chat_rompt_template = ChatPromptTemplate.from_messages(
        [
            {"role": "system", "content": "你是一个{role}"},  # 字典类型
            {"role": "human", "content": "帮我{user_input}"}
        ]
    )
    result = chat_rompt_template.format_prompt(role="翻译助手", user_input="翻译这段文字: 今天天气真好，我打算去公园散步。")
    print(result)
    print(type(result))

def chat_prompt_template_format_prompt_dev3():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import SystemMessage
    from langchain_core.messages import HumanMessage
    from langchain_core.messages import AIMessage
    # 消息类型，消息里面不能再使用变量了
    system_msg = SystemMessage(
        content="你是一个翻译助手",
        additional_kwargs={"语言": "中文、英文、日语、法语"}
    )
    human_msg = HumanMessage(content="帮我翻译下面这段文字")
    ai_msg = AIMessage(content="好的，请提供需要翻译的文本。")
    chat_msgs = [system_msg, human_msg, ai_msg]
    print("type(chat_msgs): " + str(type(chat_msgs)))
    print("chat_msgs:" + str(chat_msgs))

    # 消息类型
    chat_prompt_template = ChatPromptTemplate.from_messages(chat_msgs)
    print("chat_prompt_template:" + str(chat_prompt_template))

def chat_prompt_template_format_prompt_dev4():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_format_prompt_dev4 enter\n")
    # 元组构成的列表
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            ("human", "你好"),
            ("ai", "你好！有什么我可以帮助你的吗？"),
            ("human", "{user_input}"),
        ]
    )
    result = chat_prompt_template.format_prompt(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))

def chat_prompt_template_format_prompt_dev5():
    from langchain_core.prompts import ChatPromptTemplate
    print("chat_prompt_template_format_prompt_dev5 enter\n")
    # Chat提示词模板类型
    inner_chat_prompt_template1 = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
        ]
    )
    inner_chat_prompt_template2 = ChatPromptTemplate.from_messages(
        [
            ("human", "你好，{user_input}"),
        ]
    )

    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            inner_chat_prompt_template1,
            inner_chat_prompt_template2
        ]
    )
    result = chat_prompt_template.format_prompt(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))


def chat_prompt_template_format_prompt_dev6():
    from langchain_core.prompts import SystemMessagePromptTemplate
    from langchain_core.prompts import HumanMessagePromptTemplate
    from langchain_core.prompts import ChatPromptTemplate

    print("chat_prompt_template_format_prompt_dev6 enter\n")
    system_template = "你是一个{role}"
    system_prompt_template = SystemMessagePromptTemplate.from_template(template=system_template)

    human_template = "你好，{user_input}"
    human_prompt_template = HumanMessagePromptTemplate.from_template(template=human_template)

    # 组合成ChatPromptTemplate
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            system_prompt_template,
            human_prompt_template
        ]
    )
    result = chat_prompt_template.format_prompt(role="翻译助手", user_input="帮我翻译下面这段文字")
    print(result)
    print(type(result))



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

"""
4、消息占位符 MessagePlaceholder
使用场景：当ChatPromptTemplate模板中的消息类型和个数是动态不确定的时，使用MessagePlaceholder

"""
def chat_prompt_template_message_placeholder_dev1():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import HumanMessage
    from langchain_core.prompts import MessagePlaceholder
    print("chat_prompt_template_message_placeholder_dev1 enter\n")
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个{role}"),
            MessagePlaceholder(variable_name="messages")
        ]
    )
    result = chat_prompt_template.invoke(
        {"role": "翻译助手",
         "messages": [
            HumanMessage(content="介绍一下Transformer模型")
        ]}
    )
    print(result)
    print(type(result))

def main():
    #prompt_template_instance_dev1()
    #prompt_template_instance_dev2()

    #chat_prompt_template_invoke_dev1()
    #chat_prompt_template_format_dev1()
    #chat_prompt_template_format_messages_dev1()
    #chat_prompt_template_format_prompt_dev1()
    #chat_prompt_template_result_convert_dev1()

    #chat_prompt_template_parameter_dev1()
    #chat_prompt_template_parameter_dev2()
    #chat_prompt_template_format_prompt_dev3()
    #chat_prompt_template_format_prompt_dev4()
    #chat_prompt_template_format_prompt_dev5()
    #chat_prompt_template_format_prompt_dev6()

    #chat_message_prompt_template_dev1()

    chat_prompt_template_message_placeholder_dev1()


if __name__ == '__main__':
    main()