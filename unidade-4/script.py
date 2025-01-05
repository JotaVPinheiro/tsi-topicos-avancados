from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQA

query = input("Digite uma pergunta sobre cookies: ")

pdf_path = "aplicacoes-de-redes-de-computadores-cookies.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    length_function=len,
)
texts = text_splitter.split_documents(pages)
db = FAISS.from_documents(texts, OllamaEmbeddings(model="nomic-embed-text"))

model = OllamaLLM(model="llama3.2:3b")
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=model, retriever=retriever, chain_type="stuff"
)

response = qa_chain.invoke(query)
print("Resposta:", response["result"])
