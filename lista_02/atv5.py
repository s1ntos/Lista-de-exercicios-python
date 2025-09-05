num = []

print("Digite 10 números:")

for i in range(10):
    numeros = int(input(f"Número {i+1}: "))
    num.append(numeros)

numextra = int(input("Digite um número extra: "))

quantidade = num.count(numextra)

print(f"O número {numextra} aparece {quantidade} vezes na lista.")