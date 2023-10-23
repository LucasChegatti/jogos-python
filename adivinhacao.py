print("***************************************")
print("Bem vindo ao nosso jogo de adivinhação!")
print("***************************************")

numero_secreto = 3

chute_input = input("Digite seu numero da sorte: ")

print("Você digitou o numero: ", chute_input)

chute = int(chute_input)

if(numero_secreto == chute):
    print("Você acertou!!!")
else:
    print("Você errou!!!")

print("Fim do jogo!")

idade1 = "10"
idade2 = "20"
print(idade1 + idade2)