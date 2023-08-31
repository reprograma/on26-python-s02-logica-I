# Exerício 16

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


import math

# solicitar a área a ser pintada

area_m2 = float(input("Quantos m2 você deseja pintar? "))

# calcular quantos litros de tinta são necessários para pintar a área informada

m2_por_litro = 3      # para pintar 1m2 são necessários 3 litros de tinta

# para saber quantos litros de tinta serão necessários dividimos a área informada pela área que um litro de tinta pinta

litros_tinta = area_m2 / m2_por_litro 

print("Para pintar a área desejada serão necessários " + str(litros_tinta) + " litros de tinta")

# calcular a quantidade de latas necessárias

litros_por_lata = 18   # cada lata de tinta tem 18 litros

# para saber a quantidade de latas dividimos a quantidade de litros necessários pelos litro de uma lata
# é necessário arredondar para cima o resultado
# para isso importamos a biblioteca math (na primeira linha do programa)
# math.floor() arredonda para baixo e math.ceil() arredonda para cima

quantidade_latas = math.ceil((litros_tinta / litros_por_lata))

print("Você deverá comprar " + str(quantidade_latas) + " latas de tinta.")

# calcular o preço das latas necessárias

preco_por_lata = 80          # cada lata custa 80 reais

valor_total_latas = quantidade_latas * preco_por_lata

print("O valor da sua compra será de " + str(valor_total_latas) + " reais.")