#misturando as tintas

import math

tamanho_da_area= float(input('Digite o tamanho desejado='))
rendimento= tamanho_da_area/6
litros_com_folga= rendimento * 1.1

latas = int(litros_com_folga/18)
resto = litros_com_folga % 18
galões = math.ceil(resto/3.6)
valor_final= (latas*80) + (galões*25)


print(f'Para pintar uma área de 300m2 são necessárias {latas} latas e {galões} galões de tinta')
print(f'o preço total é de R$ {valor_final}')