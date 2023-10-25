import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("******Que os jogos comecem!******")
    print("*********************************")

    print("Escolha um dos jogos!")
    jogo = int(input("(1) Jogo de Adivinhação (2) Jogo da Forca: "))

    if(jogo == 1):
        print("Jogo de Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogo da Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()