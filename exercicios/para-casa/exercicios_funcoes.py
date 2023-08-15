#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o Segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

def soma(num_1, num_2, num_3):
    soma = num_1 + num_2 + num_3
    return soma

resultado_soma = soma(num_1, num_2, num_3)

print(f"O valor da soma de {num_1} + {num_2} + {num_3} = {resultado_soma}")