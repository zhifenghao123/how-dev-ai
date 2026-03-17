import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI



def custom_output_1():
    from langchain_core.output_parsers import PydanticOutputParser
    from pydantic.v1 import BaseModel, Field, validator
    # 优先使用环境变量中的配置
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('OPENAI_API_KEY', '')
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo-instruct')

    print(f"base_url: {base_url}, api_key: {api_key}, model: {model}")
    # 检查API密钥是否为空
    if not api_key:
        print("❌ API密钥为空，请设置 OPENAI_API_KEY 环境变量")
        return

    # 定义一个数据模型，用来描述最终输出的实例结果
    class Joke(BaseModel):
        setup: str = Field(description="设置笑话的问题")
        punch_line: str = Field(description="回答笑话的答案")

        # 验证问题是否符合要求
        @validator('setup')
        def check_setup(cls, field):
            #if field[-1] != ":":
            if field[-1] != "?" and field[-1] != "？":
                raise ValueError("不符合预期的回答格式!问题必须以问号结尾")
            return field

    # 创建一个输出解析器，用于将模型的输出转换为Joke对象
    output_parser = PydanticOutputParser(pydantic_object=Joke)

    prompt = PromptTemplate(
        template="回答用户的输入。\n{format_instructions}\n{query}",
        input_variables=["query"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()}
    )

    # 创建一个OpenAI实例
    llm = ChatOpenAI(base_url=base_url, api_key=api_key, model=model)

    prompt_and_llm = prompt | llm

    response = prompt_and_llm.invoke({"query": "给我讲一个笑话"})
    print(f"✅ AI回复: {response}")
    output_parser_invoke = output_parser.invoke(response)
    print(f"✅ 解析结果: {output_parser_invoke}")

def custom_output_2():
    from langchain_core.output_parsers import CommaSeparatedListOutputParser

    # 优先使用环境变量中的配置
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('OPENAI_API_KEY', '')
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo-instruct')

    print(f"base_url: {base_url}, api_key: {api_key}, model: {model}")
    # 检查API密钥是否为空
    if not api_key:
        print("❌ API密钥为空，请设置 OPENAI_API_KEY 环境变量")
        return

    # 创建一个输出解析器，用于将模型的输出转换为Joke对象
    output_parser = CommaSeparatedListOutputParser()

    prompt = PromptTemplate(
        template="给出10个姓郝的而且{subject}\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()}
    )

    _input = prompt.format(subject="好听的中国男生名字")

    # 创建一个OpenAI实例
    llm = ChatOpenAI(base_url=base_url, api_key=api_key, model=model)

    output = llm.invoke(_input)
    print(f"✅ AI回复: {output}")

    # 格式化输出
    output_parser_invoke = output_parser.invoke(output)
    print(f"✅ 解析结果: {output_parser_invoke}")

def main():
    # Load environment variables from .env file
    load_dotenv()

    #custom_output_1()
    custom_output_2()


if __name__ == '__main__':
    main()