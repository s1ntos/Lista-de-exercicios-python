import random

secreto = random.randint(1, 10)  
tentativas = 0

palpite = 0
while palpite != secreto:
    palpite = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1

print("Você acertou!")
print("Tentativas:", tentativas)