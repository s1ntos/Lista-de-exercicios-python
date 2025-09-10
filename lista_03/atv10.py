nome = input("Digite o nome completo: ")

partes = [p for p in nome.split() if p]  
iniciais = ".".join(p[0].upper() for p in partes) + "."
print("Iniciais:", iniciais)
