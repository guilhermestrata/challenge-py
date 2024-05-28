import tkinter as tk
from tkinter import messagebox
import random
import time

# Dados dos pilotos
nomePilotos = ['Jake', 'Stoffel', 'Sergio', 'Robin', 'Joel', 'Jake', 'Maximilian', 'Sam', 'Taylor', 'Mitch', 'Lucas', 'Antonio', 'Paul', 'Sebastien', 'Norman', 'Jehan', 'Nyck', 'Jordan', 'Oliver', 'Sacha', 'Jean-Eric', 'Dan', 'Nick', 'Edoardo', 'Nico', 'Kelvin', 'Pascal']
sobrenomePilotos = ['Dennis', 'Vandoorne', 'Sette Camara', 'Frijns', 'Eriksson', 'Hughes', 'Gunter', 'Bird', 'Barnard', 'Evans', 'Di Grassi', 'Da Costa', 'Aron', 'Buemi', 'Nato', 'Daruvala', 'De Vries', 'King', 'Rowland', 'Fenestraz', 'Vergne', 'Ticktum', 'Cassidy', 'Mortara', 'Muller', 'Van Der Linde', 'Wehrlein']
equipesPilotos = ['Andretti', 'Penske', 'ERT', 'Envision', 'Envision', 'McLaren', 'Maserati', 'McLaren', 'McLaren', 'Jaguar', 'ABT', 'Porsche', 'Envision', 'Envision', 'Andretti', 'Maserati', 'Mahindra', 'Mahindra', 'Nissan', 'Nissan', 'Penske', 'ERT', 'Jaguar', 'Mahindra', 'ABT', 'ABT', 'Porsche']

saldo = 100

def MostrarPilotos():
    lista_pilotos.delete(0, tk.END)
    for i, (nome, sobrenome) in enumerate(zip(nomePilotos, sobrenomePilotos)):
        lista_pilotos.insert(tk.END, f"{i}: {nome} {sobrenome}")

def MostrarEquipes():
    lista_equipes.delete(0, tk.END)
    for i, equipe in enumerate(equipesPilotos):
        lista_equipes.insert(tk.END, f"{i}: {equipe}")

def VerificarSaldo(moedas):
    global saldo
    if moedas > saldo:
        messagebox.showerror("Erro", "O saldo é insuficiente.")
        return False
    elif moedas < 0:
        messagebox.showerror("Erro", "Digite um número válido.")
        return False
    else:
        return True

def ConfirmacaoPositiva(confirmacao):
    return confirmacao in ['S', 's']

def AnimacaoCarregar():
    for i in range(3):
        label_status.config(text=f"Carregando{'.' * (i + 1)}")
        root.update()
        time.sleep(1)

def AnimacaoSimular():
    for i in range(3):
        label_status.config(text=f"Simulando{'.' * (i + 1)}")
        root.update()
        time.sleep(1)

def ApostarPodio(piloto1, piloto2, piloto3, moedas):
    global saldo
    indices_podio = random.sample(range(len(nomePilotos)), 3)
    podio = [(nomePilotos[i], sobrenomePilotos[i]) for i in indices_podio]

    lista_podio.delete(0, tk.END)
    for i, (nome, sobrenome) in enumerate(podio):
        lista_podio.insert(tk.END, f"Posição {i+1}: {nome} {sobrenome}")

    lista_podio_vencedor = tk.Listbox(frame_podio)
    for i, (nome, sobrenome) in enumerate(podio):
        lista_podio_vencedor.insert(tk.END, f"Posição {i+1}: {nome} {sobrenome}")
    lista_podio_vencedor.pack(side=tk.RIGHT)

    pilotos_apostados = [piloto1, piloto2, piloto3]
    acertos = sum(1 for piloto in pilotos_apostados if piloto in [nome for nome, _ in podio])

    print(acertos)

    if acertos == 3:
        saldo += 200
    elif acertos == 2:
        saldo += 100
    elif acertos == 1:
        saldo += 30
    else:
        messagebox.showinfo("Resultado", "Você perdeu :( ")
        saldo -= int(moedas * 0.60)

    label_saldo.config(text=f"Saldo: {saldo} moedas")
    return saldo



def ApostarPosicaoFinal():
    # Implementar lógica de aposta para posição final
    pass

def ApostarPitStop():
    # Implementar lógica de aposta para pit-stop mais rápido
    pass

def ApostarVoltaRapida():
    # Implementar lógica de aposta para volta mais rápida
    pass

def ApostarEquipeVencedora():
    # Implementar lógica de aposta para equipe vencedora
    pass

def exibir_categoria_podio():
    esconder_todas_frames()
    frame_podio.pack()

def exibir_categoria_posicao_final():
    esconder_todas_frames()
    frame_posicao_final.pack()

def exibir_categoria_pit_stop():
    esconder_todas_frames()
    frame_pit_stop.pack()

def exibir_categoria_volta_rapida():
    esconder_todas_frames()
    frame_volta_rapida.pack()

def exibir_categoria_equipe_vencedora():
    esconder_todas_frames()
    frame_equipe_vencedora.pack()

def esconder_todas_frames():
    frame_podio.pack_forget()
    frame_posicao_final.pack_forget()
    frame_pit_stop.pack_forget()
    frame_volta_rapida.pack_forget()
    frame_equipe_vencedora.pack_forget()

def Apostar():
    try:
        moedas = int(entry_moedas.get())
        if not VerificarSaldo(moedas):
            return

        podio = [entry_piloto1.get(), entry_piloto2.get(), entry_piloto3.get()]
        if len(podio) != 3:
            messagebox.showerror("Erro", "Selecione 3 pilotos.")
            return

        AnimacaoSimular()
        ApostarPodio(podio[0], podio[1], podio[2], moedas)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido para as moedas.")


root = tk.Tk()
root.title("Pit-Stop")
root.geometry("800x600")

# Menu principal
frame_menu = tk.Frame(root)
frame_menu.pack()

label_instrucoes = tk.Label(frame_menu, text="BOAS VINDAS AO PIT-STOP!\nEscolha uma categoria de aposta:")
label_instrucoes.pack()

button_categoria1 = tk.Button(frame_menu, text="Apostar nas posições finais dos pilotos", command=exibir_categoria_posicao_final)
button_categoria1.pack()

button_categoria2 = tk.Button(frame_menu, text="Apostar nos pilotos que estarão no pódio", command=exibir_categoria_podio)
button_categoria2.pack()

button_categoria3 = tk.Button(frame_menu, text="Apostar no tempo de pit-stop mais rápido", command=exibir_categoria_pit_stop)
button_categoria3.pack()

button_categoria4 = tk.Button(frame_menu, text="Apostar no piloto de volta mais rápida", command=exibir_categoria_volta_rapida)
button_categoria4.pack()

button_categoria5 = tk.Button(frame_menu, text="Apostar na equipe do piloto vencedor", command=exibir_categoria_equipe_vencedora)
button_categoria5.pack()

# Lista de pilotos
lista_pilotos = tk.Listbox(root)
lista_pilotos.pack(side=tk.LEFT, fill=tk.Y)

# Lista de equipes
lista_equipes = tk.Listbox(root)
lista_equipes.pack(side=tk.RIGHT, fill=tk.Y)

# Categoria: Apostar no Pódio
frame_podio = tk.Frame(root)
label_apostar = tk.Label(frame_podio, text="Apostar no Pódio:")
label_apostar.pack()

label_indice = tk.Label(frame_podio, text="Selecione o índice do piloto")
label_indice.pack()

label_piloto1 = tk.Label(frame_podio, text="Piloto 1:")
label_piloto1.pack()
entry_piloto1 = tk.Entry(frame_podio)
entry_piloto1.pack()

label_piloto2 = tk.Label(frame_podio, text="Piloto 2:")
label_piloto2.pack()
entry_piloto2 = tk.Entry(frame_podio)
entry_piloto2.pack()

label_piloto3 = tk.Label(frame_podio, text="Piloto 3:")
label_piloto3.pack()
entry_piloto3 = tk.Entry(frame_podio)
entry_piloto3.pack()

label_moedas = tk.Label(frame_podio, text="Moedas:")
label_moedas.pack()
entry_moedas = tk.Entry(frame_podio)
entry_moedas.pack()

button_apostar = tk.Button(frame_podio, text="Apostar", command=Apostar)
button_apostar.pack()

label_status = tk.Label(frame_podio, text="")
label_status.pack()

label_saldo = tk.Label(frame_podio, text=f"Saldo: {saldo} moedas")
label_saldo.pack()

lista_podio = tk.Listbox(frame_podio)
lista_podio.pack()

# Categoria: Apostar nas Posições Finais
frame_posicao_final = tk.Frame(root)
label_posicao_final = tk.Label(frame_posicao_final, text="Apostar nas Posições Finais:")
label_posicao_final.pack()

# Adicione os widgets específicos para a categoria de aposta "Posição Final"
# Adicione as entradas para os pilotos e o botão para apostar

# Categoria: Apostar no Pit-Stop Mais Rápido
frame_pit_stop = tk.Frame(root)
label_pit_stop = tk.Label(frame_pit_stop, text="Apostar no Pit-Stop Mais Rápido:")
label_pit_stop.pack()

# Adicione os widgets específicos para a categoria de aposta "Pit-Stop Mais Rápido"
# Adicione as entradas para os pilotos e o botão para apostar

# Categoria: Apostar na Volta Mais Rápida
frame_volta_rapida = tk.Frame(root)
label_volta_rapida = tk.Label(frame_volta_rapida, text="Apostar na Volta Mais Rápida:")
label_volta_rapida.pack()

# Adicione os widgets específicos para a categoria de aposta "Volta Mais Rápida"
# Adicione as entradas para os pilotos e o botão para apostar

# Categoria: Apostar na Equipe do Piloto Vencedor
frame_equipe_vencedora = tk.Frame(root)
label_equipe_vencedora = tk.Label(frame_equipe_vencedora, text="Apostar na Equipe do Piloto Vencedor:")
label_equipe_vencedora.pack()

# Adicione os widgets específicos para a categoria de aposta "Equipe do Piloto Vencedor"
# Adicione as entradas para as equipes e o botão para apostar

MostrarPilotos()
MostrarEquipes()

root.mainloop()
