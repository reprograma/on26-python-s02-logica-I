##Latas_necessárias

import math

tamanho_da_area= float(input('Digite o tamanho da área desejada='))
metros_quadrado_por_litro=3
volume_dalata= 18
preco_da_lata= 80

def calcular_o_numero_de_litros_de_tinta(tamanho_da_area, metros_quadrados_por_litro):
    numero_de_litros_de_tinta =tamanho_da_area/metros_quadrado_por_litro
    return numero_de_litros_de_tinta


# calcular quantos litros de tinta
numero_de_litros_de_tinta= tamanho_da_area/metros_quadrado_por_litro
print(f'Para pintar uma área de 300m2 são necessárias {numero_de_litros_de_tinta} litros de tinta')


#valor gasto para pintar
numero_latas = math.ceil(numero_de_litros_de_tinta/volume_dalata )
print(f'você precisa de {numero_latas} latas')

preco_final= numero_latas *preco_da_lata
print(f'o preço total é de R${preco_final}') 
