# Lista de Exercícios - Python Iniciante (Lista 1)

## Introdução
Esta lista de exercícios foi criada para iniciantes em Python que desejam praticar conceitos básicos de programação, como entrada/saída, estruturas condicionais, laços de repetição (`for` e `while`) e operações aritméticas. Cada exercício é projetado para reforçar habilidades fundamentais de programação de forma prática e direta.

Criando seu Próprio Módulo
Você pode criar seus próprios módulos para organizar o código. Suponha que você tenha um arquivo chamado meu_modulo.py com o seguinte conteúdo:

def saudacao(nome):
    print(f"Olá, {nome}!")

def soma(a, b):
    return a + b
Para usar esse módulo, basta importá-lo em outro arquivo:

import meu_modulo

meu_modulo.saudacao("Maria")
print(meu_modulo.soma(3, 4))
