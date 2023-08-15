# Importei a 'math' para poder usar 'math.ceil()', que irá arredondar para cima,
#  já que tintas são vendidas em latas inteiras
import math

# O 'input' para gerar um prompt para o usuário digitar e 'int' para converter o número digitado,
#  de string para inteiro e ser possível realizar posteriormente um cálculo
metro_quadrado_area_a_ser_pintada = int(input("Responda qual metro quadrado da área que irá pintar: "))

# A variável metro_quadrado_area_a_ser_pintada será dividida por 3, já que 1 litro cobre 3 metros quadrados,
#  'math.ceil' arredonda o resultado para cima, pois não é possível comprar a lata fracionada
quantidade_de_litros = (math.ceil(metro_quadrado_area_a_ser_pintada / 3))

# Cada lata tem 18 litros
litros_por_lata = 18

# Para ter a quantidade de latas que serão utilizadas, dividimos a quantidade de litros necessários
#  pelo número de litros em uma lata
quantidade_latas_utilizadas = (math.ceil(quantidade_de_litros / litros_por_lata))

# A quantidade de latas a serem utilizadas, é multiplicado pelo valor de cada lata
preco_lata = quantidade_latas_utilizadas * 80.00

# Imprimir o preço total da tinta, a quantidade de latas necessárias e a quantidade de litros de tinta necessários.
# O `f` serve para ajuadar na formatação
# O .2f dentro das chaves significa um pedido para ter duas casas decimais após o ponto do valor do preço
print(f"O preço da tinta será R${preco_lata:.2f} e você precisará de {quantidade_latas_utilizadas} latas. A cobertura será de {quantidade_de_litros} litros")