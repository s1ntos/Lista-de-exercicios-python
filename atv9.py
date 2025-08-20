numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0: 
    numero = int(input("Número inválido! Digite um número inteiro positivo: "))
digitos = len(str(numero))  
print(f"O número {numero} tem {digitos} dígitos")