from random import randint

Facil = {
    "De": 1,
    "Ate": 15,
    "Chances": 5
}

Medio = {
    "De": 1,
    "Ate": 20,
    "Chances": 3
}
Dificil = {
    "De": 1,
    "Ate": 25,
    "Chances": 2
}

def Iniciar(Chances, De, Ate):
    print(f"Como você escolheu a dificuldade fácil, você terá {Chances} chances e o número será de {De} até {Ate}!")
    NumeroEscolhido = randint(De, Ate)
    print("Tente acertar o número apartir de agora!")
    while(True):
        Tentativa = input("Tente: ")

        if Tentativa == NumeroEscolhido:
            print("Parabéns, você ganhou o jogo!")
            input("Pressione enter para sair!")
            quit()
        else:
            Chances -= 1
            if Chances <= 0:
                print(f"Você perdeu, o número era {NumeroEscolhido}, mais sorte na próxima vez!")
                input("Pressione enter para sair!")
                quit()
            else:
                print(f"Você errou o número, agora você possue {Chances} chances!")

print("==== Adivinhe o número ====")

while(True):
    dificuldade = input("Preciso que você escolha a dificuldade!\nFácil - (f)\nMédio - (m)\nDifícil - (d)\n")
    if len(dificuldade) == 1:
        if dificuldade in "fmd":
            break
        else:
            print("Insira corretamente a dificuldade (apenas a letra inicial)!")

if dificuldade == "f":
    Iniciar(Facil["Chances"], Facil["De"], Facil["Ate"])
if dificuldade == "m":
    Iniciar(Medio["Chances"], Medio["De"], Medio["Ate"])
if dificuldade == "d":
    Iniciar(Dificil["Chances"], Dificil["De"], Dificil["Ate"])
