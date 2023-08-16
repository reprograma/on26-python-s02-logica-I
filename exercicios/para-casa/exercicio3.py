#3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def calcular_soma(a, b, c):
    soma = a + b + c
    return soma


num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

resultado = calcular_soma(num1, num2, num3)
print(f"A soma dos três números é: {resultado}")