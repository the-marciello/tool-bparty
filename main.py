from telepot.loop import MessageLoop
import telepot, os, json, time, re
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
FILE_PATH = 'classifica.json'


def load_classifica():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_classifica(classifica):
    with open(FILE_PATH, 'w') as file:
        json.dump(classifica, file, indent=4)

def Response(msg):
    
    classifica = load_classifica()
    
    chat_id = msg['chat']['id']
    
    try:
        text = msg['text'] # squadra punteggio
        
        squadra, punteggio = text.rsplit(' ', 1)
        punteggio = int(punteggio.strip('[]'))
        
        if squadra in classifica:
            classifica[squadra] += punteggio
        else:
            classifica[squadra] = punteggio

        save_classifica(classifica)    
        bot.sendMessage(chat_id, f'Classifica aggiornata: {classifica}')
    
    except Exception as e:
        bot.sendMessage(chat_id, 'Formato messaggio non valido. Usa "{nome squadra} [punteggio]"')
    


if __name__=='__main__':
    print("Avviando...")
    classifica = load_classifica()
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, Response).run_as_thread()
    print("Avviato con successo!")
    while True:
        time.sleep(10)
