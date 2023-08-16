#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da 
# tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00. # Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

print("Digite a area a ser pintada: ")
m2_area = float(input())

litros = m2_area / 3
tamanho_lata = 18
valor_lata = 80


print ("Area a ser pintada em m2: ", m2_area)

litros_totais = m2_area / litros

qtd_latas = math.ceil(litros / tamanho_lata)
print ("Quantidade de latas a serem compradas: ", qtd_latas)

preco_total = qtd_latas * valor_lata
print("Valor total da compra: ", preco_total)





