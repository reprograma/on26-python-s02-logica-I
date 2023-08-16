#Damaris Santos Teles Brito
##Resolvido em grupo
"Resolução exercício 16 python"
"Casa de tintas"

import math

area = float(input("Digite a área a ser pintada em m²: "))
litros = area/3
latas = math.ceil(litros/18)
preco = latas * 80

print(f"Você vai precisar de {latas} latas de tinta")
print(f"O preço total é de R$ {preco:.2f}")
