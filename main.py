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

def help():
    return f'''
Buonasera! 

Se sei finito su questo bot, probabilmente è perché sei del Clan Halley!
Devi gestire un gioco? Niente di più semplice!

Manda un messaggio come questo
nomesquadra punteggio (esempio: squadra1 100)

In questo modo se non esiste una squadra con tale nome viene creata,
altrimenti i punti verranno aggiunti alla squadra


--bot sviluppato da @marcedebe
    
    '''

def Response(msg):
    
    classifica = load_classifica()
    
    chat_id = msg['chat']['id']
    text = msg['text'] # squadra punteggio
    
    if(text == "/start" or text == "/help" ):
        bot.sendMessage(chat_id, help())
    else:
        try:
            squadra, punteggio = text.rsplit(' ', 1)
            punteggio = int(punteggio.strip('[]'))
            squadra = squadra.replace(' ', '')
            
            if squadra in classifica:
                classifica[squadra] += punteggio
            else:
                classifica[squadra] = punteggio

            save_classifica(classifica)    
            bot.sendMessage(chat_id, f'Classifica aggiornata:\n {toString(classifica)}')
        
        except Exception as e:
            bot.sendMessage(chat_id, 'Formato messaggio non valido. Usa "{nome squadra} [punteggio]"')
    
def toString(classifica):
    r = ""
    i = 1
    for key, value in classifica.items():
        if value != 0:  # Controlla se il valore è diverso da zero
            r += f"{i}) {key.replace(' ', '')} - {value}\n"
            i += 1
    return r


if __name__=='__main__':
    print("Avviando...")
    
    classifica = load_classifica()
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, Response).run_as_thread()
    
    print("Avviato con successo!")
    
    while True:
        time.sleep(10)