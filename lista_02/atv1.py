def main():
    nomes = []
for i in range(10):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)

nomeprocurado = input("Qual nome você deseja procurar?")

if nomeprocurado in nomes:
    print(f"O nome {nomeprocurado} esta na lista!")
else:
    print(f"O nome {nomeprocurado} não esta na lista!")