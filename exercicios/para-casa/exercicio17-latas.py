# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
# custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário
# as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# * comprar apenas latas de 18 litros;
import math
#operações latas 
m2_por_litro = 6
lata_em_litros = 18
valor_lata = 80

#operações

print(" digite o tamanho da parede em m² a ser pintada")
litros_por_tamanho = ((float(input()) ) / m2_por_litro) 
quant_latas_comprar =  math.ceil(litros_por_tamanho / lata_em_litros )

print( "A quantidade de latas para comprar é de:" , quant_latas_comprar)

valor_compra_lata = quant_latas_comprar * valor_lata
print( "O valor a ser pago é de: $", valor_compra_lata)