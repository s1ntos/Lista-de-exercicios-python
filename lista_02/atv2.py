num = []

for i in range(5):
    numero = input(f"Digite o {i+1} numero: ")
    num.append(numero)
    
print(num[::-1])