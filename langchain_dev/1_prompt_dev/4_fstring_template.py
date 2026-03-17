"""
fstring是python内置的一种模版引擎

除此之外，Jinja2模版引擎，是一个高效，功能强大的模版引擎，可以方便地生成各种标记格式的文档。 需要引用jinja2库
"""
from langchain_core.prompts import PromptTemplate


def fstring_template1():
    fstring_template = """给我写一个关于{name}的{subject}学习计划
    谢谢"""


    # 等同于如下
    name_temp = "Mysql"
    subject_temp = "索引"
    fstring_template2 = f"给我写一个关于{name_temp}的{subject_temp}学习计划"

    prompt = PromptTemplate.from_template(fstring_template)
    result = prompt.format(name="Mysql", subject="索引")
    print(result)

    prompt2 = PromptTemplate.from_template(fstring_template2)
    result2 = prompt2.format()
    print(result2)


def main():
    fstring_template1()


if __name__ == '__main__':
    main()
