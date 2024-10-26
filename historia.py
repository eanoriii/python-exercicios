import random

def gerar_introducao():
    introducoes = ["era uma vez", "ha muito tempo atrás", "num reino distante"]
    return random.choice(introducoes)

def gerar_desenvolvimento():
    desencolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro", "uma poderosa feiticeira", "um sabio mago"]
    return random.choice(desencolvimentos)

def  gerar_conclusao():
    conclusoes = ["derrota um terrivel dragão", "conquistou o coroa", "derrotando um terrivel vilao",  "que se tornou o rei", "que venceu uma longa batalha"]
    return random.choice(conclusoes)

def  gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    conclusao = gerar_conclusao()
    historia = f"{introducao} {desenvolvimento} {conclusao}"
    return historia

if __name__ ==  "__main__":
    print(gerar_historia())



