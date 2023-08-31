# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1. comprar apenas latas de 18 litros;
# 2. comprar apenas galões de 3,6 litros;
# 3.misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# solicitar a área a ser pintada

area_m2 = float(input("Quantos m2 você deseja pintar? "))

# calcular quantos litros serão necessários para calcular a área informada

m2_por_litro = 6     # para pintar 1m2 são necessários 6 litros

# para saber quantos litros serão necessários dividimos a área informada pela área que um litro de tinta pinta

litros_tinta = area_m2 / m2_por_litro

#print("Para pintar a área desejada serão necessários " + str(litros_tinta) + " litros de tinta.")

# calcular a quantidade de latas/galões necessários

litros_por_lata = 18
litros_por_galao = 3.6

preco_lata = 80
preco_galao = 25

# para saber a quantidade de latas/galões dividimos a quantidade de litros necessários pelos litros de uma lata/galão
# necessário arredondar sempre pra cima
# para calcular o valor multiplicamos a quantidade de latas/galoes pelo preço

quantidade_latas = math.ceil((litros_tinta / litros_por_lata))
quantidade_galoes = math.ceil((litros_tinta / litros_por_galao))

valor_total_latas = quantidade_latas * preco_lata
valor_total_galoes = quantidade_galoes * preco_galao

#print("Você poderá comprar " + str(quantidade_latas) +" latas de tinta pelo valor de " + str(valor_total_latas) + " reais.")
#print("Ou " + str(quantidade_galoes) + " galões de tinta pelo valor de " + str(valor_total_galoes) + " reais.")

# misturar latas e galões (preciso voltar e rever essa parte)
