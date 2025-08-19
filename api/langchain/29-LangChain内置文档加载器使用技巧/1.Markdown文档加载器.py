from langchain_community.document_loaders import UnstructuredMarkdownLoader
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
loader = UnstructuredMarkdownLoader("./项目API资料.md")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
