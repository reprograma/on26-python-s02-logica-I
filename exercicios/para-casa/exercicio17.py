#Damaris Santos Teles Brito
##Resolvido em grupo
"Resolução exercício 17 python"
"Latas e galões" 
import math

area = float(input('Digite a área a ser pintada em m² '))
litros = area/6
litros_com_folga = litros * 1.1

latas = int(litros_com_folga/18)
resto = litros_com_folga % 18
galoes = math.ceil(resto/3.6)
preco = (latas * 80) + (galoes * 25)

print(f'Mistura de latas e galões')
print(f'Você vai precisar de  {latas} latas e {galoes} galões de tinta')
print(f'O preço total é de R$ {preco:.2f}')
