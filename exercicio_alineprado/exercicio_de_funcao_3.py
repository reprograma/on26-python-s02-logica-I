#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# CALCULADORA SIMPLES

def calculadora_simples(num1, operador, num2):
    if operador == "+":
        resultado = num1 + num2
    if operador == "-":
        resultado = num1 - num2
    if operador == "*":
        resultado = num1 * num2
    if operador == "/":
        resultado = num1 / num2
    return resultado

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

resultado = calculadora_simples(num1, operador, num2)

print(f"Resultado: {resultado}")