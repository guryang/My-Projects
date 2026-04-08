import random
import os


def limpar_tela():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')

        
print("Informe o numero maximo que deseja sortear os numeros: ")

while True:

    n = int(input())
    numero = random.randint(0,n)
    print(numero)
    
    break

limpar_tela()