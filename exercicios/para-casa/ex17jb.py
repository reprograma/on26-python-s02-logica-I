#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
# # em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

#tamanho em metro quadrado da área
area = float(input())
print("Tamanho da area em m2: ", area)

litro = 6
tamanho_lata = 18
valor_lata = 80
tamanho_galao = 3.6
valor_galao = 25


litros_totais= area / litro

litros_com_folga = litros_totais * 1.1
latas = int(litros_com_folga / tamanho_lata)
resto = litros_com_folga % tamanho_lata
galoes = math.ceil(resto/tamanho_galao )

preco = (latas * 80) + (galoes * 25)

print("Serao necessarios ", latas, "latas e ", galoes, "galoes de tinta")
print("O valor total da compra é ", preco)


