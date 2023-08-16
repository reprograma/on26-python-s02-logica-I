# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
# custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário
# as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# * comprar apenas latas de 18 litros;
# * comprar apenas galões de 3,6 litros;
# * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 
# 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
#variáveis
m2_por_litro= 6
lata_em_litros = 18
galao_em_litros = 3.6
valor_galao = 25
valor_lata = 80


#operações latas e galões

print(" digite o tamanho da parede em m² a ser pintada")
litros_por_tamanho  = ((float(input()) ) / m2_por_litro)
litros_com_folga = litros_por_tamanho * 1.1
lata = int(litros_com_folga / lata_em_litros)
resto = litros_com_folga % lata_em_litros
galao = math.ceil(resto/galao_em_litros )


print( "A quantidade de latas é ", lata , "e galões é ", galao)


valor_compra_lata_galao = (lata * valor_lata ) + (galao * valor_galao)
print( "O valor a ser pago é de: $", valor_compra_lata_galao)









