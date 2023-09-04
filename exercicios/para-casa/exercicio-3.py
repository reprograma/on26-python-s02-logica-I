# Exercício 3

# Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.

def calculo_contas_a_pagar(conta1, conta2, conta3):
    soma_contas_a_pagar = conta1 + conta2 + conta3
    return soma_contas_a_pagar

fatura_cartao = float(input("Informe o valor da fatura do cartão: "))
fatura_internet = float(input("Informe o valor da fatura da internet: "))
fatura_agua_energia = float(input("Informe o valor da fatura da água: ") + input("Informe o valor da fatura e energia: "))

total_a_pagar = calculo_contas_a_pagar(conta1=fatura_agua_energia, conta2=fatura_cartao, conta3=fatura_internet)
print("O total de contas a pagar neste mês será de " + str(total_a_pagar) + " reais.")
    