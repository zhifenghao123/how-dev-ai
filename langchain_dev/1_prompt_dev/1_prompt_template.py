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
from langchain_core.prompts import PromptTemplate

"""
字符串模板，用于LLM的提示词
"""

"""
1、PromptTemplate如何获取实例
（1）使用构造方法的方式
（2）使用from_template()方法【推荐】
"""
def prompt_template_instance_dev1():
    template = PromptTemplate(
        template="你是一个{role},请帮我{task}",
        input_variables=["role", "task"]
    )
    print(template)
    print(template.format(role="翻译助手", task="翻译这段文字"))

def prompt_template_instance_dev2():
    template = PromptTemplate.from_template(
        "你是一个{role},请帮我{task}"
    )
    print(template)
    print(template.format(role="翻译助手", task="翻译这段文字"))


"""
2、PromptTemplate两种特殊结构的使用
（1）部分提示词模版的使用（重点）
（2）组合提示词模版的使用（了解）
"""
def prompt_template_partial_dev1():
    # 方式一：在PromptTemplate的构造方法或from_template()方法中，使用partial_variables设置
    template = PromptTemplate.from_template(
        template="你是一个{role},请帮我{task}",
        partial_variables={"role": "翻译助手"}
    )
    print(template)
    print(template.format(task="翻译这段文字"))
    print(template.format(task="把这段文字翻译成法语"))
    return

def prompt_template_partial_dev2():
    # 方式一：在PromptTemplate的构造方法或from_template()方法中，使用partial_variables设置
    template = PromptTemplate(
        template="你是一个{role},请帮我{task}",
        input_variables=["task"],
        partial_variables={"role": "翻译助手"}
    )
    print(template)
    print(template.format(task="翻译这段文字"))
    print(template.format(task="把这段文字翻译成法语"))

def prompt_template_partial_dev3():
    # 方式二：调用partial()方法
    template = PromptTemplate(
        template="你是一个{role},请帮我{task}",
        input_variables=["task"],
    )

    # 调用partial()方法，设置部分变量

    # 这种方式是错误的，因为partial()方法返回的是一个新的PromptTemplate对象，而不是修改原对象
    #template.partial(role="翻译助手")

    template = template.partial(role="翻译助手")
    print(template)
    print(template.format(task="翻译这段文字"))
    print(template.format(task="把这段文字翻译成法语"))

def prompt_template_combine_dev1():
    # 组合提示词模版的使用
    template =(
        PromptTemplate.from_template(template="你是一个{role},你很善于{skill}")
        + ", 也很富有实际经验"
        + "\n\n请帮我{task}"
    )
    print(template)
    print(template.format(role="翻译助手", skill="翻译", task="翻译这段文字"))


"""
3、给变量赋值的两种方式（调用提示词模板的方式）
（1）format()：参数为各个变量，返回的是字符串
（2）invoke()：参数为包含各个变量键值对的字典，返回的是StringPromptValue对象，更建议使用这种
"""

def prompt_template_format_dev1():
    template = PromptTemplate.from_template(
        "你是一个{role},请帮我{task}"
    )
    print(template.format(role="翻译助手", task="翻译这段文字"))
    print(template.format(role="算命大师", task="算算我的命"))
    print(template.format(role="代码助手", task="帮我写个Python函数"))
    return

def prompt_template_invoke_dev1():
    template = PromptTemplate.from_template(
        "你是一个{role},请帮我{task}"
    )
    # invoke()方法返回的是StringPromptValue对象，更建议使用这种
    template_val1 = template.invoke(input={"role": "翻译助手", "task": "翻译这段文字"})
    print(type(template_val1))
    print(template_val1)
    # print(template.invoke(input={"role": "算命大师", "task": "算算我的命"}))
    # print(template.invoke(input={"role": "代码助手", "task": "帮我写个Python函数"}))
    return



def main():
    # prompt_template_instance_dev1()
    # prompt_template_instance_dev2()
    # prompt_template_partial_dev1()
    #prompt_template_partial_dev2()
    # prompt_template_partial_dev3()
    prompt_template_combine_dev1()
    # prompt_template_format_dev1()
    # prompt_template_invoke_dev1()


if __name__ == '__main__':
    main()