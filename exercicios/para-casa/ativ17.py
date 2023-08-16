# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:

# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

import math

preco_lata = 80
preco_galao = 25
cobertura = 6

tamanho = float(input('Qual o tamanho da área? '))
litros_necessarios = math.ceil(tamanho / cobertura)

#comprar apenas latas de 18 litros
qtd_latas = math.ceil(litros_necessarios / 18)
custo_latas = qtd_latas * preco_lata
print("Somente latas de 18L:")
print(f'Você precisa de {qtd_latas} lata(s), que custarão R${custo_latas:.2f}.')

# comprar apenas galões de 3.6L
qtd_galoes = math.ceil(litros_necessarios / 3.6)
custo_galoes = qtd_galoes * preco_galao
print("Somente galões de 3.6L:")
print(f'Você precisa de {qtd_galoes} galões, que custarão R${custo_galoes:.2f}.')

# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
litros_necessarios_folga = math.ceil(tamanho * 1.1 / cobertura)
qtd_latas_sobra = litros_necessarios_folga // 18
litros_restantes = litros_necessarios_folga - (qtd_latas_sobra * 18)
qtd_galoes_sobra = math.ceil(litros_restantes / 3.6)
custo_mistura = (qtd_latas_sobra * preco_lata) + (qtd_galoes_sobra * preco_galao)

print("Mistura de latas e galões:")
print(f'O cliente precisa comprar {qtd_latas_sobra} latas e {qtd_galoes_sobra} galões, que custarão R$ {custo_mistura:.2f}')