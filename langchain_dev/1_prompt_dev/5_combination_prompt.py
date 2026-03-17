"""
组合提示词，用于组合多个提示词，实现复杂的任务。
开发中涉及如下两个提示词：
（1）Final Prompt：最终返回的提示词模版
（2）Pipeline Prompt：组成提示词管道的模版，deprecated

日常中，最常用的是三层提示词设计
"""
from langchain_core.prompts import PromptTemplate


def combination_prompt1():
    full_prompt_template = """{character}
    
{behavior}
{prohibit}
    """
    full_prompt = PromptTemplate.from_template(full_prompt_template)

    # 第一层提示词，基本特性
    character_prompt_template = """你是{role}，你有着{character}。"""
    character_prompt = PromptTemplate.from_template(character_prompt_template)

    # 第二层提示词，行为规范
    behavior_prompt_template = """你遵从以下的行为：
    {behavior_list}
    """
    behavior_prompt = PromptTemplate.from_template(behavior_prompt_template)

    # 第三层提示词，禁止行为
    prohibit_prompt_template = """你不允许有以下行为：
    {prohibit_list}
    """
    prohibit_prompt = PromptTemplate.from_template(prohibit_prompt_template)

    # 使用 partial 方法组合提示词
    combined_prompt = full_prompt.partial(
        character=character_prompt.format(role="AI助手", character="专业且友好的性格"),
        behavior=behavior_prompt.format(behavior_list="1. 回答问题要准确\n\t2. 语言要简洁明了"),
        prohibit=prohibit_prompt.format(prohibit_list="1. 不提供虚假信息\n\t2. 不涉及敏感话题")
    )
    
    # 测试组合后的提示词
    print("组合提示词结果：")
    print(combined_prompt.format())
    return combined_prompt


def main():
    combination_prompt1()


if __name__ == '__main__':
    main()