#Exercicio 17 
#Apenas a 3ª alternativa foi solicitada
#Atividade realizada em grupo.

import math

area = float(input('Digite o tamanho em m2 de area a ser pintada:'))
litros = area/6
litros_com_folga = litros * 1

lata = int(litros_com_folga/18)
resto = litros_com_folga %18
galoes = math.ceil(resto/3.6)
preco = (lata*80) + (galoes*25)

print(f'Misture latas e galoes')
print(f'Você precisa de {lata} latas e {galoes} galões de tinta')
print(f'O preço total é de R$ {preco: .2f}')