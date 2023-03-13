import random

class ChatBot():
    def __init__(self, nameBot="Daun"):
        self.nameBot = nameBot

    def greetings(self):
        return random.SystemRandom().choice(["Приветствую.", "Привет.", "Рад вас видеть!"])

    def parcer(self, message):
        if message == "привет":
            return self.greetings()
        else:
            return "не понял"