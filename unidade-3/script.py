from langchain_ollama.embeddings import OllamaEmbeddings


documents = ["O rato roeu a roupa do rei de Roma"]

embeddings = OllamaEmbeddings(model="nomic-embed-text")
document_embeddings = embeddings.embed_documents(documents)

embedding_size = len(document_embeddings[0])
print(f"Tamanho dos embeddings: {embedding_size}")

formatted_first_embeddings = ", ".join(map(str, document_embeddings[0][:10]))
print(f"Embeddings: {formatted_first_embeddings}...")
