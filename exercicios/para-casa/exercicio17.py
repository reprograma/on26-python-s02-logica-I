# Exercício 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#O primeiro passo é importar a library de math pra conseguir arredondar pra cima hehehe
import math

#Input
metro_quadrado = int(input("Digite o metro quadrado da área a ser pintada: "))

#Vamos definir quantos litros serão usados
quantia_litros = (math.ceil(metro_quadrado / 6))

#Valor padrão que vem em uma lata ou galão
litro_lata = 18
litro_galao = 3.6
#Quantas latas serão utilizadas
quant_latas = (math.ceil(quantia_litros / litro_lata))
quant_galoes = (math.ceil(quantia_litros / litro_galao))
#Agora o preço padrão em uma lata
preco_tinta = quant_latas * 80.00
preco_galao = quant_galoes * 25.00

#1ª Situação:
print(f"1ª Situação: Comprar apenas latas de 18 litros:")
print(f"Você precisará de {quant_latas} latas de 18 litros.")
print(f"O preço total será de R${preco_tinta:.2f}.")

#2ª Situação
print(f"2ª Situação: Comprar apenas galões de 3,6 litros:")
print(f"Você precissará de {quant_galoes} latas de 3,6 litros.")
print(f"O preço total será de R#{preco_galao:.2f}.")

#3ª Situação: 

#Hora de calcular o volume
calc_volume = metro_quadrado / 6 * 1.1 # 10% de folga hehe

#Agora o cálculo do número mínimo necessário de ambos
quant_latas = (math.ceil(calc_volume / litro_lata))
quant_galoes = (math.ceil(calc_volume / litro_galao))

#Agora o cálculo dos preços - e também deixar as constantes aqui pra evitar ficar repetindo toda hora hehe
preco_lata_final = (math.ceil(quant_latas * preco_tinta))
preco_galao_final = (math.ceil(quant_galoes * preco_galao))
preco_apenas_latas = preco_tinta
preco_apenas_galoes = preco_galao

# Agora vamos misturar latas e galões (e calcular o custo com um galão a mais, caso necessário)
quant_latas_mistura = (math.floor(calc_volume / litro_lata))  # Completamos com latas cheias
restante = (math.ceil(calc_volume - quant_latas_mistura * litro_lata))  # Volume restante para completar com galões
quant_galoes_mistura = (math.ceil(restante / litro_galao))
preco_mistura = quant_latas_mistura * preco_apenas_latas + quant_galoes_mistura * preco_apenas_galoes

# Comparar os preços e determinar a melhor opção
if preco_apenas_latas <= preco_apenas_galoes and preco_apenas_latas <= preco_mistura:
    melhor_opcao = "apenas latas"
    preco_total = preco_apenas_latas
    quant_combinacao = quant_latas
elif preco_apenas_galoes <= preco_apenas_latas and preco_apenas_galoes <= preco_mistura:
    melhor_opcao = "apenas galões"
    preco_total = preco_apenas_galoes
    quant_combinacao = quant_galoes
else:
    melhor_opcao = "mistura de latas e galões"
    preco_total = preco_mistura
    quant_combinacao = quant_latas_mistura + quant_galoes_mistura


print(f"3ª Situação: Misturar latas e galões, de forma que o desperdício de tinta seja menor:")
print(f"A melhor opção é comprar {quant_combinacao} unidades de {melhor_opcao}")
print(f"O preço total será de R${preco_total:.2f}.")