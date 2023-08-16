# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou 
# em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços na situação:
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#area_total_m2 = x
#cobertura_tinta = y
#litros_de_tinta = (x/y)+0.1*(x/y)
#litros_latas = 18.0
#litros_galao = 3.6
# print(216%108)

# Função que calcula a quantidade de latas (quantidade) de tintas necessárias para pintar 
# (cobertura_tinta) determinada area total a ser pintada (area_total_m2)

def calculo_quantidade (area_total_m2, cobertura_tinta, volume_recipiente):
    quantidade = ((area_total_m2/cobertura_tinta)/volume_recipiente)
    return(quantidade)

area_total_m2, cobertura_tinta, volume_lata, volume_galao = {}, 6.0, 18.0, 3.6
area_total_m2 = float(input("Informe a área que será pintada em m2: "))
print(int(calculo_quantidade(area_total_m2,cobertura_tinta,volume_lata)))
ainda_faltou_cobrir = area_total_m2%108
print(ainda_faltou_cobrir)
print( "metros quadrados") #ver concat para tentar deixar tudo na mesma linha
print(round(calculo_quantidade(ainda_faltou_cobrir,cobertura_tinta, volume_galao)))