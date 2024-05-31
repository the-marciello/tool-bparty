from telepot.loop import MessageLoop
import telepot, os, json, time, re
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
TOKEN = '7439868215:AAGvEQx7ED8vyVoY4j7OqEzD-slpj5TA1xo'
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

Per creare una squadra usa il seguente comando:
/crea <nome squadra>

Per aggiungere punteggio ad una squadra usa la seguente sintassi:
<nome squadra> <punteggio> (se non esiste la squadra devi crearla!)

Per visualizzare questo messaggio usa:
/help oppure /start

Per visualizzare la classifica usa:
/classifica

--bot sviluppato da @marcedebe'''

def Response(msg):
    
    classifica = load_classifica()
    
    chat_id = msg['chat']['id']
    text = msg['text'].lower() # squadra punteggio
    
    if(text == "/start" or text == "/help" ):
        bot.sendMessage(chat_id, help())

    elif(text.startswith("/crea")):
        txt = text.split(' ', 1)

        squadra = txt[1] if len(txt) > 1 else ""

        classifica[squadra] = 0
        
        save_classifica(classifica)   

        bot.sendMessage(chat_id, f'Squadra {squadra} aggiunta!') 


    elif(text == "/classifica"):
        bot.sendMessage(chat_id, toString(classifica))

    else:
        try:
            squadra, punteggio = text.rsplit(' ', 1)
            punteggio = int(punteggio.strip('[]'))
            squadra = squadra.replace(' ', '')
            
            if squadra in classifica:
                classifica[squadra] += punteggio
            else:
                bot.sendMessage(chat_id, f'Squadra {squadra} non trovata, per aggiungerne una nuova usa /crea ' + '{nome squadra}')

            save_classifica(classifica)    
            bot.sendMessage(chat_id, f'Classifica aggiornata:\n {toString(classifica)}')
        
        except Exception as e:
            bot.sendMessage(chat_id, 'Formato messaggio non valido. Usa "{nome squadra} [punteggio]"')
    
def toString(classifica):
    r = ""
    i = 1
    for key, value in classifica.items():
        if(not 'fyreck' in key):
        # if value != 0:  # Controlla se il valore è diverso da zero
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