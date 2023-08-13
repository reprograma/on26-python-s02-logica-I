# Faça um programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# A tinta é vendida em latas de 18 litros, que custam R$ 80,00
# Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total

def calculo_quantidade (area_total, cobertura_tinta, volume_lata):
    quantidade = ((area_total/cobertura_tinta)/volume_lata)
    return(quantidade)

area_total, cobertura_tinta, volume_lata = {}, 3.0, 18.0
area_total = (float(input("Insira a área em m2 que será pintada: ")))
quantidade = ((area_total/cobertura_tinta)/volume_lata)
print("Você irá precisar de ")
print(quantidade)
print("latas")