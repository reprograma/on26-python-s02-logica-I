# Faça um programa, com uma função que necessite de três argumentos 
# e que forneça a soma desses três argumentos.

#Definindo a funcao (valor da compra de 3 itens)
def compra(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    return soma


valor1 = float(input('Digite o valor1: '))
valor2 = float(input('Digite o valor2: '))
valor3 = float(input('Digite o valor3: '))

#Chamando a funcao
valor_total = compra(valor1, valor2, valor3)
print(f' O valor total da compra é R$: {valor_total:.2f}')
