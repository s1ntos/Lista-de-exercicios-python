def main():
    num = []

    print("Digite todos os números de 1 a 12")

    for i in range(12):
        numeros = int(input(f"Número {i+1}:"))
        num.append(numeros)

    print(num[::-2])



if __name__ == "__main__":
    main()