# Faça um programa, com uma função que necessite de três argumentos, e
# que forneça a soma desses três argumentos.

def soma(n1, n2, n3):
    calculo_soma = n1 + n2 + n3
    return calculo_soma


print('Adicione os números para somar')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

print('Soma = ', soma(n1, n2, n3))