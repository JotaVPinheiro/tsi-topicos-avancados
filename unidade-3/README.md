# Passos para rodar o script

## Garantir que o Python e o PIP estejam instalados

```sh
python -v
pip -v
```

## Instalar a lib Python `langchain_ollama`

```sh
pip install langchain_ollama
```

## Garantir que o [Ollama](https://ollama.com/) esteja instalado

```sh
ollama -v
```

## Instalar o model de embedding `nomic-embed-text`

```sh
ollama pull nomic-embed-text
```
