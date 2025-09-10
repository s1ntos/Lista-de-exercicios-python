texto = input("Digite uma palavra ou frase: ")

vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"A quantidade de vogais na string é: {contador}")
