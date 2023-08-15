#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#1. comprar apenas latas de 18 litros;
#2. comprar apenas galões de 3,6 litros;
#3. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def quant_total_latas(area_total):
    litros_total = (area_total/6)*1.1                      # Quantidade de litros para ser distribuída entre as latas de 18l e de 3,6l (incluídos os 10% de folga)
    quant_latas_grandes = int(litros_total//18)
    quant_latas_pequenas = round(((litros_total % 18)/3.6) + 0.5)
    custo_total = (quant_latas_grandes*80) + (quant_latas_pequenas*25)
    return quant_latas_grandes, quant_latas_pequenas, custo_total

area_total = float(input("Área em m² a ser pitada: "))

print("A quantidade de latas de 18l, a quantidade de latas de 3,6l a serem compradas e o valor total a ser pago são, respectivamente:", quant_total_latas(area_total))




