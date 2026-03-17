"""
实现一个自定义的PromptTemplate。
函数解释器：根据函数名称，查找函数代码，并给出中文的代码说明
"""
from typing import Any

from langchain_core.prompts import StringPromptTemplate


def add(a, b):
    added = a + b
    print(f"add {a} + {b} = {added}")
    return added

def generate_request_id():
    import uuid
    # 以当前时间戳为基准，生成一个随机的请求ID
    return str(uuid.uuid4())

def print_current_time():
    import datetime
    now = datetime.datetime.now()
    print(f"当前时间: {now}")


PROMPT = """
你是一个经验丰富的程序员，现在给你如下函数名称，你回按照如下格式，输出这个函数的名称、源代码和中文代码说明。
函数名称: {function_name}
源代码:
{source_code}
代码解释:
"""

def get_source_code(function_name):
    # 获取函数源代码
    import inspect
    return inspect.getsource(function_name)

# 自定义PromptTemplate
class CustomPromptTemplate(StringPromptTemplate):

    def format(self, **kwargs: Any) -> str:
        # 获取函数源代码
        source_code = get_source_code(kwargs["function_name"])

        # 格式化提示词
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__,
            source_code=source_code
        )
        return prompt

def main():
    custom_prompt = CustomPromptTemplate(input_variables=["function_name"])
    prompt_msg = custom_prompt.format(function_name=add)
    print(prompt_msg)


    print("="*20)
    prompt_msg = custom_prompt.format(function_name=generate_request_id)
    print(prompt_msg)

    print("="*20)
    prompt_msg = custom_prompt.format(function_name=print_current_time)
    print(prompt_msg)

if __name__ == "__main__":
    main()

