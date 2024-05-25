import random
import time



nomePilotos = ['Jake', 'Stoffel', 'Sergio',
               'Robin', 'Joel', 'Jake',
               'Maximilan', 'Sam', 'Taylor', 
               'Mitch', 'Lucas', 'Antonio', 
               'Paul', 'Sebastien', 'Norman', 
               'Jehan', 'Nyck', 'Jordan', 
               'Oliver', 'Sacha', 'Jean-Eric', 
               'Dan', 'Nick', 'Edoardo', 
               'Nico', 'Kelvin', 'Pascal']

sobrenomePilotos = ['Dennis', 'Vandoorne', 'Sette Camara',
                    'Frijns', 'Eriksson', 'Hughes',
                    'Gunter', 'Bird', 'Barnard',
                    'Evans', 'Di Grassi', 'Da Costa',
                    'Aron', 'Buemi', 'Nato', 
                    'Daruvala', 'De Vries' 'King',
                    'Rowland', 'Fenestraz', 'Vergne',
                    'Ticktum', 'Cassidy', 'Mortara',
                    'Muller', 'Van Der Linde', 'Wehrlein']

numerosPilotos = [1, 2, 3, 4, 4, 5, 7, 8, 8, 9, 11, 13, 16,
                  16, 17, 18, 21, 21, 22, 23, 25, 33, 37, 48,
                  51, 51, 94]

equipesPilotos = ['Andretti', 'Penske', 'ERT',
                  'Envision', 'Envision', 'McLarem',
                  'Maseratti', 'McLarem', 'McLarem',
                  'Jaguar', 'ABT', 'Porsche',
                  'Envision', 'Envision', 'Andretti',
                  'Maseratti', 'Mahindra', 'Mahindra',
                  'Nissan', 'Nissan', 'Penske',
                  'ERT', 'Jaguar', 'Mahindra',
                  'ABT', 'ABT', 'Porsche']

def MostrarPilotos():
    for i in range(len(nomePilotos) - 1):
        print( '+-------------------------------------+')
        print(f'|                 {i}                 |')
        print(f'|NOME: {nomePilotos[i]} {sobrenomePilotos[i]}\n|EQUIPE: {equipesPilotos[i]}')

def MostrarEquipes():
    for i in range(len(equipesPilotos) - 1):
        print( '+-------------------------------------+')
        print(f'|                 {i}                 |')
        print(f'|EQUIPE: {equipesPilotos[i]}'           )

print('BOAS VINDAS AO PIT-STOP!')

print('+-----------------------------------------------------+')
print('|                     INSTRUCOES:                     |')
print('+-----------------------------------------------------+')
print('| 1. Escolha um piloto para apostar;                  |')
print('| 2. Aposte suas moedas nas categorias disponiveis;   |')
print('| 3. Inicie a simulacao e aguarde o resuldado;        |')
print('+-----------------------------------------------------+')
print('|#####################################################|')
print('+-----------------------------------------------------+')
print('|               CATEGORIAS DE APOSTAS:                |')
print('+----+------------------------------------------------+')
print('| 1. | Apostar nas posicoes finais dos pilotos;       |')
print('| 2. | Apostar nos pilotos que estarão no podio;      |')
print('| 3. | Apostar no tempo de pit-stop mais rapido;      |')
print('| 4. | Apostar no piloto de volta mais rapida;        |')
print('| 5. | Apostar na equipe do piloto vencedor           |')
print('+----+------------------------------------------------+')


def AnimacaoCarregar():
    palavra = 'Carregando'
    pontos = ''
    for i in range(3):
        pontos += '.'
        print(f'{palavra}{pontos}')
        time.sleep(1)

def AnimacaoSimular():
    palavra = 'Simulando'
    pontos = ''
    for i in range(3):
        pontos += '.'
        print(f'{palavra}{pontos}')
        time.sleep(1)

def ValidarPosicao(posicao):
    if posicao > len(nomePilotos) - 1:
        return False
    elif posicao < 0:
        return False
    else:
        return True

def ConfirmacaoPositiva(confirmacao):
    if confirmacao == 'S' or confirmacao == 's':
        return True
    else:
        return False

def ConfirmacaoNegativa(confirmacao):
    if confirmacao == 'N' or confirmacao == 'n':
        return True
    else:
        return False

def FichaAposta(categoria, valor):
    print('+-------------------------------------+')
    print('|          FICHA DE CONFIRMACAO       |')
    print('|                                     |')
    print(f'|Categoria: {categoria}                         |')
    print(f'|Valor da aposta: {valor}                  |')
    print('+-------------------------------------+')

saldo = 100

def VerificarSaldo(moedas):
    if moedas > saldo:
        print('O saldo é insuficiente.')
        return False
    elif moedas < 0:
        print('Digite um numero valido')
        return False
    else:
        return True

def ApostarPosicaoFinal(posicao, moedas):
    global saldo
    posicaoFinal = random.randint(1, len(nomePilotos) + 1)
    if posicao == posicaoFinal:
        print('Parabens voce acertou!')
        saldo += moedas * 0.5
    else:
        print('Voce perdeu :( ')
        saldo -= moedas

    return saldo


def ApostarPodio(piloto1, piloto2, piloto3, moedas):
    podio = random.sample(nomePilotos, 3)

    acertos = 0
    if piloto1 in podio and piloto1 != podio[0]:
        acertos += 1
    if piloto2 in podio and piloto2 != podio[1]:
        acertos += 1
    if piloto3 in podio and piloto3 != podio[2]:
        acertos += 1

    if acertos == 3:
        saldo += 200
    elif acertos == 2:
        saldo += 100
    elif acertos == 1:
        saldo += 30
    else:
        print('Você perdeu :( ')
        moedas -= int(moedas * 0.60)

    return podio, acertos, moedas
def ApostarEquipe(equipe, moedas):
    equipeVencedora = random.sample(equipesPilotos, 1)
    if equipe in equipeVencedora:
        print('Parabens voce venceu"  :)')
        moedas += 300
    else:
        print('Voce perdeu :(')
        moedas -= moedas * 0.7
    return vencedor, moedas

def ApostarPitStop(piloto, moedas):
    vencedor = random.sample(nomePilotos, 1)
    if piloto in vencedor:
        print('Parabens você venceu! :)')
        moedas += 300
    else:
        print('Voce perdeu :(')
        moedas -= moedas * 0.7
    return vencedor, moedas

def ApostarVoltaRapida(piloto, moedas):
    vencedor = random.sample(nomePilotos, 1)
    if piloto in vencedor:
        print('Parabens você venceu! :)')
        moedas += 300
    else:
        print('Voce perdeu :(')
        moedas -= moedas * 0.7
    return vencedor, moedas

categoria = int(input("Selecione o numero da respectiva categoria de aposta: "))

if categoria == 1:
    while True:
        print('Categoria selecionada: Apostar nas posicoes finais dos pilotos\n')
        AnimacaoCarregar()
        MostrarPilotos()
        piloto = int(input("Selecione o indice do piloto que deseja apostar: "))
        print(f'Piloto selecionado: {nomePilotos[piloto]} {sobrenomePilotos[piloto]}')
        posicao = int(input("Em qual posicao este piloto ficará? (n): "))
        if ValidarPosicao(posicao):
            moedas = int(input(f"Quantas moedas deseja apostar em {nomePilotos[piloto]} {sobrenomePilotos[piloto]}?"))
            if VerificarSaldo(moedas):
                FichaAposta(1, moedas)
                confirmacao = input('Prosseguir para a simulacao?: (S/n)')
                if ConfirmacaoPositiva(confirmacao):
                    AnimacaoSimular()
                    saldoAtual = ApostarPosicaoFinal(posicao, moedas)
                    print('Saldo atual: ', saldoAtual)
                    time.sleep(2)
                    prosseguir = input('Deseja apostar de novo?: (S/n)')
                    if ConfirmacaoNegativa(prosseguir):
                        print('OBRIGADO POR JOGAR!\n ATÉ A PROXIMA     :)')
                        break
                else:
                    time.sleep(2)
                    print('Aposta encerrada...')
                    break
            else:
                print('Programa encerrado...')
                break
elif categoria == 2:
    while True:
        print('Categoria selecionada: Apostar nos pilotos que estarão no podio\n')
        AnimacaoCarregar()
        MostrarPilotos()
        podio = []
        for i in range(1, 4):  
            piloto = int(input(f'\nSelecione o piloto que ficara em {i} lugar: '))
            podio.append(f'{nomePilotos[piloto]} {sobrenomePilotos[piloto]}')
        print('Seu podio ficou:\n')
        for p in podio:
            print(p)
        moedas = int(input(f"Quantas moedas deseja apostar no podio?"))
        if VerificarSaldo(moedas):
            FichaAposta(2, moedas)
            time.sleep(0.5)
            confirmacao = input('Prosseguir para a simulacao?: (S/n)')
            if ConfirmacaoPositiva(confirmacao):
                AnimacaoSimular()
                resultado, acertos, saldo = ApostarPodio(podio[0], podio[1], podio[2], moedas)
                time.sleep(2)
                print(f"Resultado do podio: {resultado}")
                print(f"Número de acertos: {acertos}")
                print(f"Saldo de moedas após a aposta: {saldo}")
                prosseguir = input('Deseja apostar de novo?: (S/n)')
                if ConfirmacaoNegativa(prosseguir):
                    print('OBRIGADO POR JOGAR!\n ATÉ A PROXIMA     :)')
                    break
            else:
                time.sleep(2)
                print('Aposta encerrada...')
                break
        else:
            print('Programa encerrado...')
            break

elif categoria == 3:
    while True:
        print('Categoria selecionada: Apostar no tempo de pit-stop mais rapido\n')
        AnimacaoCarregar()
        MostrarPilotos()
        piloto = int(input("Selecione o indice do piloto que deseja apostar: "))
        print(f'Piloto selecionado: {nomePilotos[piloto]} {sobrenomePilotos[piloto]}')
        moedas = int(input(f"Quantas moedas deseja apostar no podio?"))
        if VerificarSaldo(moedas):
            FichaAposta(2, moedas)
            time.sleep(0.5)
            confirmacao = input('Prosseguir para a simulacao?: (S/n)')
            if ConfirmacaoPositiva(confirmacao):
                AnimacaoSimular()
                vencedor, saldo = ApostarPitStop(piloto, saldo - moedas)
                time.sleep(2)
                print(f'Piloto com Pit-Stop mais rapido: {vencedor}')
                print(f'Saldo de moedas apos aposta: {saldo:.2f}')
                prosseguir = input('Deseja apostar de novo?: (S/n)')
                if ConfirmacaoNegativa(prosseguir):
                    print('OBRIGADO POR JOGAR!\n ATÉ A PROXIMA     :)')
                    break
            else:
                time.sleep(2)
                print('Aposta encerrada...')
                break
        else:
            print('Programa encerrado...')
            break
elif categoria == 4:
    while True:
        print('Categoria selecionada: Apostar no piloto de volta mais rapida\n')
        AnimacaoCarregar()
        MostrarPilotos()
        piloto = int(input("Selecione o indice do piloto que deseja apostar: "))
        print(f'Piloto selecionado: {nomePilotos[piloto]} {sobrenomePilotos[piloto]}')
        moedas = int(input(f"Quantas moedas deseja apostar no podio?"))
        if VerificarSaldo(moedas):
            FichaAposta(2, moedas)
            time.sleep(0.5)
            confirmacao = input('Prosseguir para a simulacao?: (S/n)')
            if ConfirmacaoPositiva(confirmacao):
                AnimacaoSimular()
                vencedor, saldo = ApostarPitStop(piloto, saldo - moedas)
                time.sleep(2)
                print(f'Piloto com Pit-Stop mais rapido: {vencedor}')
                print(f'Saldo de moedas apos aposta: {saldo:.2f}')
                prosseguir = input('Deseja apostar de novo?: (S/n)')
                if ConfirmacaoNegativa(prosseguir):
                    print('OBRIGADO POR JOGAR!\n ATÉ A PROXIMA     :)')
                    break
            else:
                time.sleep(2)
                print('Aposta encerrada...')
                break
        else:
            print('Programa encerrado...')
            break
elif categoria == 5:
    while True:
        print('Categoria selecionada: Apostar na equipe do piloto vencedor\n')
        AnimacaoCarregar()
        MostrarEquipes()
        equipe = int(input("Selecione o indice da equipe em que deseja apostar: "))
        print(f'Equipe selecionada: {equipesPilotos[equipe]}')
        moedas = int(input(f"Quantas moedas deseja apostar no podio?"))
        if VerificarSaldo(moedas):
            FichaAposta(2, moedas)
            time.sleep(0.5)
            confirmacao = input('Prosseguir para a simulacao?: (S/n)')
            if ConfirmacaoPositiva(confirmacao):
                AnimacaoSimular()
                equipeVencedora, saldo = ApostarEquipe(equipe, moedas)
                print(f'Equipe vencedora: {equipeVencedora}')
                print(f'Saldo de moedas apos aposta: {saldo:.2f}')
                prosseguir = input('Deseja apostar de novo?: (S/n)')
                if ConfirmacaoNegativa(prosseguir):
                    print('OBRIGADO POR JOGAR!\n ATÉ A PROXIMA     :)')
                    break
            else:
                time.sleep(2)
                print('Aposta encerrada...')
                break
        else:
            print('Programa encerrado...')
            break
else:
    print('Escolha nao disponivel...')


