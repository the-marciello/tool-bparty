# DEPRECATED

import tkinter as tk
import json

def load():
    with open('classifica.json', 'r') as file:
        dati = json.load(file)

    lista_tuple = [(k, v) for k, v in dati.items()]

    matrice = []

    for coppia in lista_tuple:
        matrice.append(list(coppia))


if __name__ == '__main__':
    window = tk.Tk()

    window.configure(bg='black')

    window.geometry("160x190")
    #window.attributes("-fullscreen", True)
    window.mainloop()
