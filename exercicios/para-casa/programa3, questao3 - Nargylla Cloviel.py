#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#Para tornar um pouco mais interessante, vamos fazer um programa que retornar o valor em reais que a pessoa acumulou ao longo de
# três meses.

apresentacao = "Olá, boas vindas a sua calculadora Money!"
print(apresentacao)
info1 = "Por favor, insira o valor que você adquiriu durante os três últimos meses"
mes1 = float(input("insira o valor do mês 1: "))
mes2 = float(input("insira o valor do mês 2: "))
mes3 = float(input("insira o valor do mês 3: "))

resultado = mes1 + mes2 + mes3
print("O valor arrecadado foi de") 
print (resultado)