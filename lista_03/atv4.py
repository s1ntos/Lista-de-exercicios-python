palavra = input("Digite uma palavra: ")

norm = palavra.replace(" ", "").lower()

inv = ""
for ch in norm:
    inv = ch + inv

if norm == inv:
    print("É palíndromo ")
else:
    print("Não é palíndromo ")
