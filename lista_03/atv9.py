texto = input("Digite um texto: ")

letras = numeros = espacos = 0

for ch in texto:
    if ch.isalpha():
        letras += 1
    elif ch.isdigit():
        numeros += 1
    if ch.isspace():
        espacos += 1

print(f"Letras:  {letras}")
print(f"Números: {numeros}")
print(f"Espaços: {espacos}")