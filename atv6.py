soma = 0
contador = 0

numero = int(input("Agora você vai digitar 5 números, Digite o primeiro: "))
soma += numero
contador += 1

while contador < 5:
    numero = int(input(("Digite o proximo: ")))
    soma += numero
    contador += 1

print("A soma dos números é:", soma)


