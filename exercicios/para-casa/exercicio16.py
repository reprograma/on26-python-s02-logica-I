# Tamanho em metros quadrados da area a ser pintada

import math

metros_quadrados = float(input())

# Cobertura da tinta é de um litro para cada três metros quadrados

metro_quadrado_por_litro = 3
litros_lata = 18
valor_lata = 80

#Calculo do litro de tinta necessária
litros = metros_quadrados / metro_quadrado_por_litro
print(litros)

# Quantidade de tintas a serem compradas
quantidade_latas = math.ceil(litros / litros_lata)
print(quantidade_latas)


# Preço total da compra das latas de tinta
valor_total = quantidade_latas * valor_lata
print(valor_total)