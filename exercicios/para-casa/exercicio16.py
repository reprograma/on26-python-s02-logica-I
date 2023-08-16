#Exercício 16

import math
preco_lata= 80.00

metros_quadrados = float(input("Informe a o tamanho da área a ser pintada:"))

metros_quadrados_litro = 3
lata_capacidade_litros = 18

total_de_litros = metros_quadrados / metros_quadrados_litro

#Informe  o tamanho da área a ser pintada:

print(total_de_litros)

quantidade_de_latas = math.ceil (total_de_litros / lata_capacidade_litros) 
print("O total de latas a serem compradas é:", quantidade_de_latas)

preco_a_pagar_latas = quantidade_de_latas * preco_lata

print("O preco total a pagar",  preco_a_pagar_latas)