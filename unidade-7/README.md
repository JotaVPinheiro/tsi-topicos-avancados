# O que este script faz?

O script realiza a trancrição de um arquivo de audio fornecido utilizando o Whisper e, utilizando o Ollama, gera um resumo com os pontos chaves dess conteúdo.

# Passos para rodar o script

## Garantir que o Python e o PIP estejam instalados

```sh
python -v
pip -v
```

## Instalar as libs Python `openai-whisper` e `langchain_ollama`

```sh
pip install openai-whisper langchain_ollama
```

## Garantir que o [Ollama](https://ollama.com/) esteja instalado

```sh
ollama -v
```

## Instalar o model LLM `llama3.2:3b`

```sh
ollama pull llama3.2:3b
```

## Executar o script

```sh
python script.py
```

# Exemplos de uso:

## Entrada:

\* Letra de Never Gonna Give You Up do Rick Astley \*

## Saída:

Aqui estão os pontos-chave do texto:

**Introdução**

- A canção "Never Gonna Give You Up" é uma declaração de amor e compromisso.
- O cantor afirma que está disposto a dar todo o seu amor e atenção ao parceiro.

**Reafirmação do amor**

- O cantor reitera sua intenção de nunca abandonar o parceiro.
- Ele promete não fazer mal ao parceiro, nem mesmo se isso significa dizer "goodbye" ou mentir.

**Conhecimento compartilhado**

- O cantor e o parceiro sabem que o outro está se sentindo do mesmo modo.
- Eles estão "jogando a mesma partida", apesar de não terem dito nada abertamente.

**Reafirmação do amor**

- O cantor repete sua declaração de amor e compromisso multiple vezes.
- A canção é uma expressão apaixonada e sincera do amor pelo parceiro.

**Mensagem final**

- A canção termina com a promessa de nunca deixar o parceiro sozinho.
- O cantor parece estar dizendo que está pronto para viver a vida ao lado do parceiro, sem hesitar ou abandoná-lo.
