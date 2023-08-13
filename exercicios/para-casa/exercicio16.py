# Exercício 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#O primeiro passo é importar a library de math pra conseguir arredondar pra cima hehehe
import math

#Input
metro_quadrado = int(input("Digite o metro quadrado da área a ser pintada: "))

#Vamos definir quantos litros serão usados
quantia_litros = (math.ceil(metro_quadrado / 3))

#Valor padrão que vem em uma lata
litro_lata = 18

#Quantas latas serão utilizadas
quant_latas = (math.ceil(quantia_litros / litro_lata))

#Agora o preço padrão em uma lata
preco_tinta = quant_latas * 80.00

#Finalmente, o print com o adicional do cálculo de coberturas pq estava me sentindo aventureira hihi
print(f"O preço da tinta será R${preco_tinta} e você precisará de {quant_latas} latas. A cobertura será de {quantia_litros} litros")
