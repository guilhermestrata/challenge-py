import tkinter as tk
from tkinter import messagebox
import random
import time

# Importando as funções do arquivo funcoes.py
from main import *

class CasaDeApostasFE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Casa de Apostas - Fórmula E")

        self.label = tk.Label(self, text="Bem-vindo à Casa de Apostas - Fórmula E")
        self.label.pack(pady=10)

        self.frame_aposta = tk.Frame(self)
        self.frame_aposta.pack(pady=10)

        self.label_aposta = tk.Label(self.frame_aposta, text="Faça sua Aposta:")
        self.label_aposta.pack(side=tk.LEFT, padx=10)

        self.entry_aposta = tk.Entry(self.frame_aposta)
        self.entry_aposta.pack(side=tk.LEFT)

        self.button_apostar = tk.Button(self, text="Apostar", command=self.realizar_aposta)
        self.button_apostar.pack(pady=10)

    def realizar_aposta(self):
        valor_aposta = self.entry_aposta.get()
        categoria = random.randint(1, 5)  # Escolha aleatória da categoria de aposta
        resultado = ApostarPitStop(valor_aposta, categoria)
        messagebox.showinfo("Aposta Realizada", resultado)

if __name__ == "__main__":
    app = CasaDeApostasFE()
    app.mainloop()
