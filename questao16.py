# Questão 16

import math
# math usa para arrendondar

def new_func():
    area = float(input('Digite o tamanho em m² de area para pintar: ='))
    return area

area = new_func()
litros = area/3
latas = math.ceil(litros/18) 
#levando em consideracao que cada lata tem 18l
preco = latas * 80

print ('quantidade' , latas , 'latas de tinta')
print('o preco total em R$' , str (preco))

