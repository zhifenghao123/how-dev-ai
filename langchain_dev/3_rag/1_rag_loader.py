from dotenv import load_dotenv


# 使用loader加载Markdown文件
def text_loader():
    from langchain_community.document_loaders import TextLoader
    loader = TextLoader("res/LLM_vs_ChatModel.md")
    docs = loader.load()
    print(docs)


def csv_loader():
    from langchain_community.document_loaders import CSVLoader
    #loader = CSVLoader("res/llm.csv")
    loader = CSVLoader(file_path="res/llm.csv", source_column="模型名称")
    docs = loader.load()
    print(docs)


def excel_loader_1():
    from langchain_community.document_loaders import UnstructuredExcelLoader

    # 首先需要pip install unstructured
    # 以及随后需要根据报错依次安装networkx、pandas、msoffcrypto
    loader = UnstructuredExcelLoader("res/llm.xlsx")
    docs = loader.load()
    print(docs)

def excel_loader_2():
    from langchain_community.document_loaders import DirectoryLoader
    # 首先需要pip install unstructured
    # 以及随后需要根据报错依次安装networkx、pandas、msoffcrypto

    # 这种方式可以把指定目录下所有xlsx文件都加载进来
    loader = DirectoryLoader("res/", glob="*.xlsx")
    docs = loader.load()
    print(docs)

def pdf_loader():
    from langchain_community.document_loaders import PyPDFLoader

    # 首先需要pip install pdfminer
    loader = PyPDFLoader("res/llm.pdf")
    pdf = loader.load()
    print(pdf)

    print("\npdf_pages")
    pdf_pages = loader.load_and_split()
    print(pdf_pages)


def html_loader():
    from langchain_community.document_loaders import UnstructuredHTMLLoader
    loader = UnstructuredHTMLLoader("res/LLM_vs_ChatModel.html")
    html = loader.load()
    print(html)

def json_loader():
    from langchain_community.document_loaders import JSONLoader
    
    # 需要先pip install jq
    #loader = JSONLoader("res/llm.json", jq_schema='.[].models[].name')
    loader = JSONLoader("res/llm.json", jq_schema='.[].company')
    json = loader.load()
    print(json)

def main():
    # load_dotenv()
    #text_loader()
    #csv_loader()
    # excel_loader_1()
    #excel_loader_2()
    #pdf_loader()
    #html_loader()
    json_loader()


if __name__ == '__main__':
    main()