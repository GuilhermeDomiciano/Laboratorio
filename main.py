import funcoes
from funcoes import *

print("Bem vindo ao meu Programa em python!")
print("Escolha uma das opções para começar:")
print("\t.1 Jogo de adivinhação")
print("\t.2 Banco de dados")
print("\t.0 Para sair do código")
qt_op = 2

while True:
    op = int(input("Escolha uma das opções: "))

    if op == 0:
        print("Saindo do código. Até mais!")
        break

    if op == 1:
        print("Você escolheu Jogo de adivinhação!")
        jogo_de_adivinhacao()
        print("\t1. Jogo de adivinhação")
        print("\t2. Banco de dados")
        print("\t0. Para sair do código")

    if op == 2:
        print("Você escolheu Banco de dados!")
        banco_de_dados()
        print("\t1. Jogo de adivinhação")
        print("\t2. Banco de dados")
        print("\t0. Para sair do código")

    else:
        print("Opção inválida. Escolha uma das opções abaixo:")
        print("\t1. Jogo de adivinhação")
        print("\t2. Banco de dados")
        print("\t0. Para sair do código")