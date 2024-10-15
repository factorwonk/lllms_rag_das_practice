
def replace_t_with_space(documents):
    """
    Replaces all tab characters ('\t') with spaces in the page content of each document.

    Args:
        list_of_documents: A list of document objects, each with a 'page_content' attribute.

    Returns:
        The modified list of documents with tab characters replaced by spaces.
    """

    for doc in documents:
        doc.page_content = doc.page_content.replace("\t", " ")
    return documents