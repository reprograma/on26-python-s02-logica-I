# Questão 17 - Faça um Programa para uma loja de tintas.

import math 

area = float(input(" Insira o tamanho da area em metros quadrados = "))
litros = area/6
litros_com_folga = litros * 1.1 

lata = int(litros_com_folga/18)
resto = litros_com_folga % 18
galoes = math.ceil(resto/3.6)
preco = (lata *80) + (galoes * 25)

print(f"Misture latas e galoes")
print(f"Você precisa de {lata} latas e {galoes} galoes de tinta")
print(f"O preço total é de R$ {preco:.2f}")