from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
