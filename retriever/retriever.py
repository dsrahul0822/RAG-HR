def get_retriever(vectorstore, k=3):
    """
    Get the retriever for the vectorstore
    """
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever