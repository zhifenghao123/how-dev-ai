"""
文档切割
原理
1. 将文档分成小的、有意义的块（句子）•
2. 将小的块组合成一个更大的块，直到达到一定的大小.
3. 一旦达到一定的大小，接着开始创建与下一个块重叠的部分.

示例
- 第一个文档分割
- 按字符切割
- 代码文档切割
- 按token来切割
"""


def document_simple_split():
    """
    文档简单分割
    :return:
    """
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    with open("res/LLM_vs_ChatModel.txt", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,    # 切分文本块的大小，一般通过长度函数计算
        chunk_overlap=20,   # 分文本块之间的重叠大小，一般通过长度函数计算
        length_function=len,  # 长度函数，用于计算文本块的长度，也可以传递tokenize函数
        add_start_index=True  # 是否添加起始索引
    )
    # chunks = splitter.split_text(text)
    # print(chunks)

    docs = splitter.create_documents([text])
    print(docs)
    for doc in docs:
        print(doc)

def document_split_by_character():
    """
    按照字符分割
    :return:
    """
    from langchain_text_splitters import CharacterTextSplitter
    with open("res/LLM_vs_ChatModel.txt", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = CharacterTextSplitter(
        separator="\n",  # 切割的分隔符，默认是\n\n
        chunk_size=100,  # 切分文本块的大小，一般通过长度函数计算
        chunk_overlap=20,  # 分文本块之间的重叠大小，一般通过长度函数计算
        length_function=len,  # 长度函数，用于计算文本块的长度，也可以传递tokenize函数
        add_start_index=True,  # 是否添加起始索引
        is_separator_regex=False  # 是否将分隔符作为正则表达式处理
    )
    docs = splitter.create_documents([text])
    print(docs)
    for doc in docs:
        print(doc)

def document_split_for_program_code():
    """
    代码文档分割
    :return:
    """
    from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

    print("支持的语言有：")
    for e in Language:
        print(str(e.value))

    with open("res/langchain_example.py", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = RecursiveCharacterTextSplitter.from_language(
        Language.PYTHON,
        chunk_size=100,
        chunk_overlap=20,
        add_start_index=True,
    )
    docs = splitter.create_documents([text])
    print(docs)

def document_split_by_token():
    """
    按照token分割
    :return:
    """
    from langchain_text_splitters import TokenTextSplitter
    with open("res/LLM_vs_ChatModel.txt", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = TokenTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        add_start_index=True,
    )
    docs = splitter.create_documents([text])
    print(docs)

def document_split_by_token_2():
    """
    按照token分割
    :return:
    """
    from langchain_text_splitters import CharacterTextSplitter
    with open("res/LLM_vs_ChatModel.txt", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=150,
        chunk_overlap=20,
        add_start_index=True,
    )
    docs = splitter.create_documents([text])
    print(docs)

def main():
    #document_simple_split()
    #document_split_by_character()
    #document_split_for_program_code()
    #document_split_by_token()
    document_split_by_token_2()

if __name__ == '__main__':
    main()