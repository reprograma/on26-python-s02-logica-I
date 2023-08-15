# Faça um Programa para uma loja de tintas. O programa deverá pedir 
# o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

## Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços na seguinte situação:
### misturando latas e galões, de forma que o desperdício de tinta seja menor. 
### Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

print("Seja bem vinde! Use este programa para calcular a quantidade de tinta que será necessária para a sua pintura")

from math import ceil

tamanho_da_area = float(input("Informe a área a ser pintada em m² "))

cobertura_tinta_emlitros = tamanho_da_area / 6
cobertura_com_folga = (cobertura_tinta_emlitros * 1.1)

quantidade_latas = (cobertura_com_folga // 18)
sobra = (cobertura_com_folga % 18)
quantidade_galoes = ceil(sobra / 3.6)

valor_latas = quantidade_latas * 80
valor_galoes = quantidade_galoes * 25
valor_total = valor_latas + valor_galoes

print("Você precisará de", quantidade_latas, "latas e", quantidade_galoes, "galões.")
print("O valor total será de", valor_total, "reais.")




