# Faça um programa, 
# com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos. 

def calcular_soma(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    print("A soma é igual a ", soma)

valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))
calcular_soma(valor1, valor2, valor3)
