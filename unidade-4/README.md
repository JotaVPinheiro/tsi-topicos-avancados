# O que este script faz?

O script recebe uma pergunta do usuário relacionada ao assunto de cookies e a partir de uma base de dados vetorial com embeds gerados a partir de chunks de um documento pdf sobre o assunto, utiliza um retriever para gerar uma resposta para a pergunta

# Passos para rodar o script

## Garantir que o Python e o PIP estejam instalados

```sh
python -v
pip -v
```

## Instalar as libs Python `langchain_community`, `langchain_ollama`, `pypdf` e `faiss-cpu`

```sh
pip install langchain_community langchain_ollama pypdf faiss-cpu
```

## Garantir que o [Ollama](https://ollama.com/) esteja instalado

```sh
ollama -v
```

## Instalar o model de embedding `nomic-embed-text`

```sh
ollama pull nomic-embed-text
```

## Instalar o model LLM `llama3.2:3b`

```sh
ollama pull llama3.2:3b
```

## Executar o script

```sh
python script.py
```

# Exemplos de perguntas e respostas:

## P: O que são cookies?

R: Cookies são pequenas metadatas que os sites web enviam ao navegador do usuário para armazenar informações sobre a visita, como preferências de usuário, carrinhos de compra, etc. Essas informações são armazenadas em um local seguro no dispositivo do usuário e são enviadas automaticamente quando o usuário visita novamente o mesmo site ou outros sites relacionados.
