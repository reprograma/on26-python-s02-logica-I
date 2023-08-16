#Se 1 litro pinta 3 metros quadrados, então uma lata com 18litros vai pintar  54. 
# Logo, a cada x metros quadrados, você divide por 54. Por exemplo, se você tem 108 metros 
# quadrados, você vai dividir por 54, que dá 2, então você precisa de duas latas de tintas!
# Se você tiver 120, quando dividido por 54, 
# da aproximadamente 2,22 , então você vai precisar de 3 latas, já que 2 não será suficiente

#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura 
# da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.


import math
#variáveis
m2_por_litro = 3
lata_em_litros = 18
valor_lata = 80

#operações

print(" digite o tamanho da parede em m² a ser pintada")
litros_totais_por_tamanho = ((float(input()) ) / m2_por_litro)
quant_latas_comprar = math.ceil(litros_totais_por_tamanho / lata_em_litros)
print( "A quantidade de latas para comprar é de:" , quant_latas_comprar)

valor_compra = quant_latas_comprar * valor_lata
print( "O valor a ser pago é de: $", valor_compra)

