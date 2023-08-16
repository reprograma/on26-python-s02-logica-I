#Questão 16, feito um parte em grupo. 

import math

areaPintarM2 = float(input("Qual a medida da área que deseja pintar? "))

quantDem2PorLitros = 3.0
quantDeLitrosNaLata = 18.0
totalValorLata = 80.0

litrosDeTinta = math.ceil(areaPintarM2 / quantDem2PorLitros)
quantDeLatas = math.ceil(litrosDeTinta / quantDeLitrosNaLata)
if litrosDeTinta % 18 != 0:
    quantDeLatas += 1 #incremento

valorTotalCompra = math.ceil(quantDeLatas * totalValorLata)

print(f"Você vai precisar de {quantDeLatas} latas de tinta")
print(f"O preço total é de R$ {valorTotalCompra:.2f}")

