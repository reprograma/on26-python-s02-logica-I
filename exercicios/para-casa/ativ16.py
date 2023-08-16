# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.

import math

area_a_ser_pintada = float(input('Quantos m² serão pintados? '))

litros_de_tinta = area_a_ser_pintada / 3
lata_de_tinta = math.ceil(litros_de_tinta / 18)
preco = lata_de_tinta * 80

print(f'Você deverá comprar {lata_de_tinta} lata(s) de tinta')
print(f'O total é R$ {preco:.2f}')