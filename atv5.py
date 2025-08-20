nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ") 
senha1 = input("Digite novamente sua senha: ")

while senha1 != senha:
    print("Senha incorreta. Tente novamente.")
    senha1 = input("Digite novamente sua senha: ")  

print("Seja bem-vindo", nome)