# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

print("Bem vinde! Use este programa para calcular a quantidade de tinta que será necessária para a sua pintura")

from math import ceil

tamanho_da_area = float(input("Informe a área a ser pintada em m² "))

cobertura_tinta_emlitros = tamanho_da_area / 3

quantidade_latas = ceil(cobertura_tinta_emlitros / 18)

print("Você vai precisar de ", quantidade_latas, "lata(s)")

valor = quantidade_latas * 80

print("O valor total será", valor, "reais")