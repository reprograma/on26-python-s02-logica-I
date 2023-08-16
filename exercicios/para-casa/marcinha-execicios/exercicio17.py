
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.





import math

area = float(input('Digite o tamanho em m² de area a ser pintada: '))
litros = area/6
litros_com_folga = litros * 1.1

lata = int(litros_com_folga/18)
resto = litros_com_folga % 18
galoes = math.ceil(resto/3.6)
preco = (lata * 80) + (galoes * 25)

print(f'Misture latas e galões')
print(f'Você precisa de {lata} latas e {galoes} galoes de tinta')
print(f'O preço total é de R$ {preco:.2f}')



#exercicios feito em grupo de estudos