# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18L, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

cobertura_de_tinta_por_metro_quadrado = 3
capacidade_litros_por_lata_de_tinta = 18
preco_por_lata = 80

tamanho_da_area = float (input("digite aqui o tamanho da area que deseja pintar(em m²)"))

litros = tamanho_da_area/cobertura_de_tinta_por_metro_quadrado
lata_cheia = float(litros/capacidade_litros_por_lata_de_tinta)
if litros%lata_cheia != 0:
 lata_cheia += 1

valor_total = lata_cheia*preco_por_lata

print("Quantidade de litros de tinta a serem usados:", litros)
print("Quantidade de latas de tinta a serem usadas:", lata_cheia)
print("Preço total da compra: R$", preco_por_lata)





