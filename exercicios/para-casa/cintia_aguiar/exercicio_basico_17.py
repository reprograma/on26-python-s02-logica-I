#Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;

#Essa parte aqui EU NÃO TENHO IDEIA DE COMO FAZER...
#misturar latas e galões, de forma que o desperdício de tinta seja menor
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


#Quantidade de m² que o litro de tinta faz
metro_quadrado_por_litro = 6

#Tamanho da lata de tinta em litros
tamanho_da_lata_em_litros = 18
preco_da_lata = 80.00

#Tamanho em galões
tamanho_do_galao_em_litros = 3.6
preco_do_galao = 25.00

#Solicitação ao usuário do tamanho da área
metro_quadrados_a_pintar = float(input("Digite o tamanho da área a ser pintada em m²: "))

#Cálculo da quantidade de litros de tinta necessários
#dividindo a área pela cobertura por litro
litros_necessarios = metro_quadrados_a_pintar / metro_quadrado_por_litro

#Calculo da quant de latas que o usuario vai precisar
#Dividindo a quant de litros pelo tamanho de cada lata
quantidade_de_latas = litros_necessarios / tamanho_da_lata_em_litros
if litros_necessarios % tamanho_da_lata_em_litros != 0:
    quantidade_de_latas = int(quantidade_de_latas) + 1

#Calculo da quant de galoes que o usuario vai precisar
#Dividindo a quant de litros pelo tamanho de cada galao
quantidade_de_galoes = litros_necessarios / tamanho_do_galao_em_litros
if litros_necessarios % tamanho_do_galao_em_litros != 0:
    quantidade_de_galoes = int(quantidade_de_galoes) + 1

#Cálculo do preço total das latas multiplicando a quantidade de latas pelo valor de cada lata
preco_total_latas = quantidade_de_latas * preco_da_lata
print(f"Comprando apenas latas, você precisará de {quantidade_de_latas:.0f} latas de tinta.") #formato em nº inteiro
print(f"E o valor total será de R$ {preco_total_latas:.2f}") #formato em 2 casas decimais

#Cálculo do preço total dos galões multiplicando a quantidade de galões pelo valor de cada galão
preco_total_galoes = quantidade_de_galoes * preco_do_galao
print(f"Comprando apenas galões, você precisará de {quantidade_de_galoes:.0f} galões de tinta.") #formato em nº inteiro
print(f"E o valor total será de R$ {preco_total_galoes:.2f}") #formato em 2 casas decimais