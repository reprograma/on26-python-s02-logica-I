# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1 - comprar apenas latas de 18 litros;
# 2 - comprar apenas galões de 3,6 litros
# 3 - misturar latas e galões, de forma que o desperdício de tinta seja menor.
# 4 - Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print("LOJA DE TINTAS")

area_em_metros_quadrados_a_serem_pintados= int(input('Quantos m² pretende pintar? --> '))
litros = (area_em_metros_quadrados_a_serem_pintados / 6) * 1.1
latas = math.ceil(litros / 18)
preco_por_lata = latas * 80
galao = math.ceil(litros / 3.6)
preco_por_galao = galao * 25 

mistura_de_latas = round(litros / 18)
mistura_de_galoes = round((litros - mistura_de_latas * 18) / 3.6)

if((litros - (mistura_de_latas * 18) % 3.6 != 0)):
    mistura_de_galoes += 1 
    total_de_misturas = (mistura_de_latas * 80) + (mistura_de_galoes * 25)

    print(f'Se for compar só latas de 18L irá precisar de {latas} latas e irá custar R$ {preco_por_lata:.2f}')
    print(f'Se for compar só galões de 3,6L irá precisar de {galao} galão(ões) e irá custar R$ {preco_por_galao:.2f}')  
    print(f'se deseja misturar latas e galões para dar o que precisa realmente será necessário {mistura_de_latas} lata(s) 'f'e {mistura_de_galoes} galã0(ões) e irá custar R$ {total_de_misturas:.2f}')

    