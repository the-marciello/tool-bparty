import tkinter as tk
import json
class ScoreBoardGUI:
    window = tk.Tk()

    window.geometry("160x190")

    window.title("SCOREBOARD")

    window.resizable(False, False)

    window.configure(background="white")
    # uncomment this line to activate fullscreen mode
    # window.attributes("-fullscreen", True)

    if __name__ == "__main__":
        window.mainloop()