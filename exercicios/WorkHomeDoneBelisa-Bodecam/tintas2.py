import math

area = float(input("Digite o tamanho em M² de area a ser pintado "))
litros = area/6
litros_com_folga = litros * 1.1

latas = int(litros_com_folga/18)
resto = litros_com_folga % 18
galoes = math.ceil(resto/3.6)
preco = (latas * 80) + (galoes * 25)

print(f"Misture latas e galões")
print(f"Você precisa de {latas} latas e {galoes} galões de tinta ")
print(f"O preço total é de R$ {preco:.2f}")