# Exerício 16

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# solução utilizando função

# criando função vai calcular o número de litros tintas

import math

def calcular_numero_litros(numero_metro_quadrado, area_por_litro):
    numero_litros = numero_metro_quadrado / area_por_litro
    return numero_litros

# variáveis criadas

area_m2 = float(input("Quantos m2 você deseja pintar? "))
m2_por_litro = 3
litros_por_lata = 18 
preco_por_lata = 80 

# chamando a função para calcular

litros_tinta = calcular_numero_litros(numero_metro_quadrado=area_m2, area_por_litro=m2_por_litro)
print(litros_tinta)

# criando funções para calcular a quantidade de lata e preço final

def calcular_numero_latas(numero_litros_tinta, litros_por_lata):
    numero_latas = numero_litros_tinta / litros_por_lata
    return numero_latas

def calcula_preco_final(numero_latas, preco_por_lata):
    preco_final = numero_latas * preco_por_lata
    return preco_final

# chamando as funções para calcular

quantidade_latas = math.ceil(calcular_numero_latas(numero_litros_tinta=litros_tinta, litros_por_lata=litros_por_lata))
valor_total = math.ceil(calcula_preco_final(numero_latas=quantidade_latas, preco_por_lata=preco_por_lata))

print("Você deverá comprar " + str(quantidade_latas) + " latas de tinta.")
print("O valor da sua compra será de " + str(valor_total) + " reais.")

    