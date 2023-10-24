print("***************************************")
print("Bem vindo ao nosso jogo de adivinhação!")
print("***************************************")

numero_secreto = 3
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    chute_input = input("Digite seu numero da sorte entre 1 e 100: ")
    print("Você digitou o numero: ", chute_input)
    chute = int(chute_input)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue

    chute_certo = chute == numero_secreto
    chute_menor = chute < numero_secreto
    chute_maior = chute > numero_secreto

    if(chute_certo):
        print("Você acertou!!!")
        break
    else:
        if(chute_menor):
            print("Você errou! O seu chute foi menor que o numero secreto!")
        elif(chute_maior):
            print("Você errou! O seu chute foi maior que o numero secreto!")

print("Fim do jogo!")
