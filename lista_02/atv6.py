
lista = []
for i in range(5):  
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)


valor = int(input("Digite o valor que deseja procurar: "))

encontrado = False
for i in range(len(lista)):
    if lista[i] == valor:
        print(f"O valor {valor} aparece no índice {i}")
        encontrado = True

if not encontrado:
    print(f"O valor {valor} não aparece na lista.")
