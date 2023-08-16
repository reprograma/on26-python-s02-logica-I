## Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

## Solicitar entrada do usuário para os três números

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

## Chamar a função para obter a soma

resultado = somar_tres_numeros(num1, num2, num3)

## Exibir o resultado

print(f"A soma dos três números é: (resultado)")