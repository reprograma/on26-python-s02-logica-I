#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def contas_do_mes(luz, internet, aluguel):
    soma_das_contas = luz + internet + aluguel
    return soma_das_contas

luz, internet, aluguel = float(input("Valor da conta de luz: ")), float(input("Valor da conta de internet: ")), float(input("Valor do aluguel: "))

print("Valor total a pagar:", contas_do_mes(luz, internet, aluguel))


