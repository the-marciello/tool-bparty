import telepot
from telepot.loop import MessageLoop
import json
import threading
import os

# Token del tuo bot
TOKEN = '7439868215:AAGvEQx7ED8vyVoY4j7OqEzD-slpj5TA1xo'
FILE_PATH = 'classifica.json'

class ClassificaBot:
    def __init__(self, token, file_path):
        self.bot = telepot.Bot(token)
        self.file_path = file_path
        self.classifica = self.load_classifica()

    def load_classifica(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_classifica(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.classifica, file, indent=4)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            try:
                text = msg['text']
                name, score = text.rsplit(' ', 1)
                score = int(score.strip('[]'))
                if name in self.classifica:
                    self.classifica[name] += score
                else:
                    self.classifica[name] = score
                self.save_classifica()
                self.bot.sendMessage(chat_id, f'Classifica aggiornata: {self.classifica}')
            except Exception as e:
                self.bot.sendMessage(chat_id, 'Formato messaggio non valido. Usa "{nome squadra} [punteggio]"')

    def run(self):
        MessageLoop(self.bot, self.handle).run_as_thread()
        while True:
            pass

if __name__ == '__main__':
    bot = ClassificaBot(TOKEN, FILE_PATH)
    threading.Thread(target=bot.run).start()
