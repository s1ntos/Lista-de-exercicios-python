qtd = int(input("Quantos nomes você deseja digitar? "))

nomes = []
for i in range(qtd):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

print("\nLista original:", nomes)


antigo = input("\nQual nome você deseja substituir? ")

if antigo in nomes:
    novo = input("Digite o novo nome: ")
    indice = nomes.index(antigo)
    nomes[indice] = novo
    print("\nLista atualizada:", nomes)
else:
    print("\nEsse nome não está na lista.")