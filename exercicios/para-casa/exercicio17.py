# Tamanho em metros quadrados da area a ser pintada
import math


metros_quadrados = int(input())

# Cobertura da tinta é de um litro para cada três metros quadrados

metro_quadrado_por_litro = 6
litros_lata = 18
valor_lata = 80
litros_galao = 3.6
valor_galao = 25

#Calculo do litro de tinta necessária
litros = metros_quadrados / metro_quadrado_por_litro
print(litros)

litros_com_folga = litros * 1.1
print(litros_com_folga)


# Misturar latas e galões. Acrescente 10% de folga e arredonde os valores para cima
quantidade_lata_folga = int(litros_com_folga / litros_lata)
resto = litros_com_folga % litros_lata
quantidade_galao_folga = math.ceil(resto / litros_galao)
preco = (quantidade_lata_folga * valor_lata) + (quantidade_galao_folga * valor_galao)

print(quantidade_lata_folga)
print(resto)
print(quantidade_galao_folga)
print(f'o preço total é de {preco: .2f}')