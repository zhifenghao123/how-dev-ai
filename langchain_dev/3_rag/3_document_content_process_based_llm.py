import os

from dotenv import load_dotenv


def transform_pdf_content_by_llm():
    """
    使用LLM对PDF内容进行转换
    :return:
    """
    pdf_content = ["我是一个程序员"]

    # 需要先pip install doctran
    from langchain_core.embeddings import Embeddings

    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('OPENAI_API_KEY', '')
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo-instruct')


    embeddings = Embeddings()
    query = embeddings.embed_documents(pdf_content)
    print(query)


def main():
    load_dotenv()
    transform_pdf_content_by_llm()

if __name__ == '__main__':
    main()