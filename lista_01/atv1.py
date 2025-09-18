num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par")
else:

    print("O número é ímpar")




def main():
    """Ecoa os argumentos de entrada para a saída padrão."""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main()) 
