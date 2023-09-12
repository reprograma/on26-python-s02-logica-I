#Faça um programa, com uma função que necessite de três argumentos
#e que forneça a soma desses três argumentos.

numero1 = 10
numero2 = 20
numero3 = 30

def soma_tres_numeros(a, b, c):
    resultado = a + b + c
    return resultado

resultado_soma = soma_tres_numeros(numero1, numero2, numero3)
print("A soma dos três números é:", resultado_soma)