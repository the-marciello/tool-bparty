import json
import tkinter as tk

# Funzione per aggiornare la classifica
def update_leaderboard():
    # Carica i dati dal file JSON
    with open('classifica.json', 'r') as file:
        data = json.load(file)

    # Trasforma i dati in una lista di tuple e ordina per punteggio
    classifica = sorted(data.items(), key=lambda item: item[1], reverse=True)

    # Aggiungi il rank
    classifica = [(i + 1, squadra, punteggio) for i, (squadra, punteggio) in enumerate(classifica)]

    # Elimina tutti i widget attualmente presenti nella finestra
    for widget in frame.winfo_children():
        widget.destroy()

    # Crea le intestazioni
    header = tk.Label(frame, text=f"{'RANK':<6} {'PLAYER NAME':<15} {'SCORE':<5}", bg='black', fg='#90EE90', font=('Courier', 50, 'bold'))
    header.pack()

    # Inserisci i dati nella tabella con un loop
    for rank, player, score in classifica:
        if rank == 1:
            fg_color = 'yellow'
        elif 2 <= rank <= 5:
            fg_color = 'red'
        else:
            fg_color = '#ADD8E6'
        
        entry = tk.Label(frame, text=f"{rank:<6} {player:<15} {score:<5}", bg='black', fg=fg_color, font=('Courier', 50, 'bold'))
        entry.pack()

    # Richiama nuovamente la funzione dopo 0.1 secondi
    root.after(100, update_leaderboard)

if __name__ == '__main__':
    # Crea la finestra principale
    root = tk.Tk()
    root.title("Classifica")
    root.configure(bg='black')

    # Crea un titolo
    title = tk.Label(root, text="CLASSIFICA", bg='black', fg='#90EE90', font=('Courier', 90, 'bold'))
    title.pack(pady=10)

    # Crea un frame per contenere la tabella
    frame = tk.Frame(root, bg='black')
    frame.pack(pady=10)

    # Avvia l'aggiornamento iniziale
    update_leaderboard()
    
    root.attributes("-fullscreen", True)
    
    # Avvia la finestra principale
    root.mainloop()
