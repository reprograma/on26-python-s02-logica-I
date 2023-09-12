#Faça um programa para uma loja de tintas
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Quantidade de m² que o litro de tinta faz
metro_quadrado_por_litro = 3

#Tamanho da lata de tinta em litros
tamanho_da_lata_em_litros = 18
preco_da_lata = 80.00

#Solicitação ao usuário do tamanho da área
metro_quadrados_a_pintar = float(input("Digite o tamanho da área a ser pintada em m²: "))

#Cálculo da quantidade de litros de tinta necessários
#dividindo a área pela cobertura por litro
litros_necessarios = metro_quadrados_a_pintar / metro_quadrado_por_litro

#Calculo da quant de latas que o usuario vai precisar
#Dividindo a quant de litros pelo tamanha de cada lata
quantidade_de_latas = litros_necessarios / tamanho_da_lata_em_litros
if litros_necessarios % tamanho_da_lata_em_litros != 0:
    quantidade_de_latas = int(quantidade_de_latas) + 1

#IF linha 24 - verifica se o calculo anterior é diferente de zero ou seja se há quant fracionaria
#Linha 25 se if for true arredanda para cima. Converte o valor em nº inteiro e add +1

#Cálculo do preço total multiplicando a quantidade de latas pelo valor de cada lata
preco_total = quantidade_de_latas * preco_da_lata

print(f"Você precisará de {quantidade_de_latas:.0f} latas de tinta.") #formato em nº inteiro
print(f"O preço total é de R$ {preco_total:.2f}") #formato em 2 casas decimais