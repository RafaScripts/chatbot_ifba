# chat atendimento da policia
#### codigo constuido para atividade avaliativa da matéria de Inteligiancia Artificial


## Objetivo
O objetivo do projeto é criar um chatbot que simule um atendimento da policia, onde o usuário pode fazer perguntas e o chatbot irá responder de acordo com a pergunta feita.


## Funcionamento
O chatbot foi construido utilizando a biblioteca Chatterbot, que é uma biblioteca de aprendizado de máquina baseada em regras para responder perguntas em linguagem natural. O chatbot foi treinado com algumas perguntas e respostas, e a partir disso ele consegue responder perguntas feitas pelo usuário.


## Como usar
para utilizar o chatbot em modo terminal basta executar o arquivo `robo.py`, mas antes deve executar o treinamento do mesmo `treinamento.py`, para que o chatbot seja treinado com as perguntas e respostas.

para utilizar com interface gráfica siga os passos:

1. entre na pasta chat/

2. instale as dependencias do node:
```bash
npm install
```
ou
```bash
yarn install
```
ou
```bash
pnpm install
```

3. inicie o servidor:
```bash
npm start
```

4. inicie o serviço do chatbot:

```bash
python servico.py

**ps: lembre de executar esse comando na mesma pasta em que se encontra o arquivo

```

5. acesse o endereço `http://localhost:3000/` no seu navegador

a partir daqui ja pode executar suas pergundas e o chatbot irá responder de acordo com o treinamento feito.


## Treinamento
O treinamento do chatbot foi feito com perguntas e respostas que podem ser encontradas no arquivo `treinamento.py`, para treinar o chatbot basta executar o arquivo `treinamento.py` e ele irá treinar o chatbot com as perguntas e respostas que estão no arquivo.


## Tecnologias utilizadas
- Python
- Chatterbot
- Node.js
- Socket.io


## Videos

- [Video de apresentação](https://youtu.be/f-ktIwy2_xA)

## Licença
MIT
```