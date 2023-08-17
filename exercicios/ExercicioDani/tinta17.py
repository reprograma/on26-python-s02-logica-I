metros = float(input("Quantos metros quadrados deseja pintar?", ))

latasg = (metros)/108
latasm = (metros)/21.6
latase = (metros)


def verificar_numero(tinta18):
    if tinta18 % 1 == 0:
        print("Optando por latas grandes de 18 litros cada, você irá precisar de:", int(tinta18), " latas e pagará R$", int(tinta18)*80,".")
    else:
        print("Optando por latas grandes de 18 litros cada, você irá precisar de:", int(tinta18) + 1, "latas e pagará R$", (int(tinta18)+1)*80,".")

tinta18 = float(latasg)
verificar_numero(tinta18)

def verificar_numero(tinta3):
    if tinta3 % 1 == 0:
        print("Optando por latas médias de 3,6 litros cada, você irá precisar de:", int(tinta3), " latas e pagará R$", int(tinta3)*25,".")
    else:
        print("Optando por latas médias de 3,6 litros cada, você irá precisar de:", int(tinta3) + 1, "latas de 3,6 litros e pagará R$", (int(tinta3)+1)*25,".")

tinta3 = float(latasm)
verificar_numero(tinta3)

import math

# latas
metros_a_ser_pintada = (metros)
area_com_folga = metros_a_ser_pintada * 1.1
numero_de_latas = math.ceil((metros)/108)
litros_por_metros = 6
litro_a_ser_usado = math.ceil(area_com_folga/litros_por_metros)
litros_por_latas = 18 
preco_latas = numero_de_latas *80
#print(litro_a_ser_usado, numero_de_latas, preco_latas)

# Galao

numero_de_galao = math.ceil((metros)/21.6)
litro_a_ser_usado = math.ceil(area_com_folga/litros_por_metros)
litros_por_galao = 3.6
preco_galao = numero_de_galao*25
#print(litro_a_ser_usado, numero_de_galao, preco_galao)

#Mistura
numero_de_lata = math.floor(litro_a_ser_usado / litros_por_latas)
preco_de_latas = numero_de_lata * 80
litros_faltante = litro_a_ser_usado % litros_por_latas

numero_de_galoes = math.floor(litros_faltante/litros_por_galao)
valor_galoes = numero_de_galoes * 25
valor_total = preco_de_latas + valor_galoes

print(f"Para otimizar sua compra, sugerimos que compre {numero_de_lata} latas e  {numero_de_galoes} em galões e pague apenas R${valor_total}")







