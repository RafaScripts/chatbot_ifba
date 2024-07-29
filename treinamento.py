from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CHATS = [
    "/home/Rafael/Desktop/prj/chatbot_ifba/conversas/saudacoes.json",
    "/home/Rafael/Desktop/prj/chatbot_ifba/conversas/informacoes_basicas.json"
]

def start():
    robot = ChatBot("Robô de Atendimento da Polícia")
    treining = ListTrainer(robot)

    return treining

def load_chats():
    chats = []

    for file_chats in CHATS:
        with open(file_chats, "r") as file:
            chats_to_treining = json.load(file)
            chats.append(chats_to_treining["conversas"])

            file.close()

    return chats

def train(treining, chats):
    for chat in chats:
        for chat_responses in chat:
            messages = chat_responses["mensagens"]
            response = chat_responses["resposta"]

            print(f"treinando o robô. Mensagens: {messages}. Resposta: {response}")
            for message in messages:
                treining.train([message, response])


if __name__ == "__main__":
    training = start()

    chats = load_chats()
    if chats:
        train(training, chats)
