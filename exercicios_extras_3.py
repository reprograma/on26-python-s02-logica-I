# 4. Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# e ‘N’, se seu argumento for zero ou negativo.

def calculo(valor):
    if valor > 0:
        print("P")
    else: print("N")

valor = float(input("Informe o valor: "))

calculo(valor)