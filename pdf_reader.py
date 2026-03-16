from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("report.pdf")

documents = loader.load()