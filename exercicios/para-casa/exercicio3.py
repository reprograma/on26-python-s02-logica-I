# Exercício 3 - Faça um programa, com uma função que necessite de três argumentos,  e que forneça a soma desses três argumentos.
def a_pagar_calc(valor1, valor2, valor3):
    soma = (valor1 + valor2 + valor3)
    return soma

print ("Digite o valor da sua conta de luz:")
valor1 = (float(input()))
print ("Digite o valor da sua conta de água:")
valor2 = (float (input()))
print ("Digite o valor da sua conta de interrnet:")
valor3 = (float (input()))

print (f"No fim do mês, o valor total que você pagará é de: R${a_pagar_calc(valor1, valor2, valor3):.2f}")

