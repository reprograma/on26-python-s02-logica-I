#### Exercícios Básicos
#https://wiki.python.org.br/EstruturaSequencial 
#Exercícios para entregar: 16 e 17

#16.Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#variaveis
metro_quadrado = float(input("Quantos metros quadrados tem a sua casa? "))
cobertura_tinta = metro_quadrado * 3
lata_de_tinta_litros = 18
valor_da_lata_tinta_reais = 80

if metro_quadrado > 0:
    x = cobertura_tinta / lata_de_tinta_litros  #encontrar quantas latas de tintas
    y = int(x) + 1  # Arredonda para cima o número de latas necessárias
    valor_total = y * valor_da_lata_tinta_reais
    print(f"Você irá comprar {y} latas de tinta, e o valor total será de {valor_total:.2f} reais.")
else:
    print("Erro: O tamanho da área deve ser maior que zero.")


#17.Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#variaveis
metro_quadrado = float(input("Quantos metros quadrados tem a sua casa? "))
cobertura_tinta = metro_quadrado * 6 #calculo da cobertura de tinta
lata_de_tinta_litros = 18 #metro quadrado de lata 
valor_da_lata_tinta_reais = 80 # valor da lata
galao_de_tintas_litros = 3.6 # galãode litros
valor_galao_de_tinta_reais = 25 #valor do galão 
#mistura entre as tintas 
quantidade_latas_mistura = int(cobertura_tinta / lata_de_tinta_litros) #achar a qauntidade de latas
quantidade_galoes_mistura = int((cobertura_tinta - quantidade_latas_mistura * lata_de_tinta_litros) / galao_de_tintas_litros) # achar a quantidade de galões - latas de mistura

#primeiro if para mostrar quantas latas 18 litros que iremos usar e qual valor
if metro_quadrado > 0 and metro_quadrado > 3.6:
    x = cobertura_tinta/lata_de_tinta_litros
    y = int(x) + 1
    valor_total = y * valor_da_lata_tinta_reais
    print(f"Você irá comprar {y} latas de tintas de 18 litros, e custará {valor_total} em reais")
#segundo if somente para encontrar a quantidade dos galões e o seu valor
if metro_quadrado > 0 and metro_quadrado >= 3.6:
    x = cobertura_tinta/galao_de_tintas_litros
    y = int(x)+1
    valor_total = y * valor_galao_de_tinta_reais
    print(f"Você irá comprar {y} galões de tintas de 3,6 litros, e custará {valor_total} em reais")
#terceiro if que mostra a mistura dos dois galões
if (cobertura_tinta - quantidade_latas_mistura * lata_de_tinta_litros) % galao_de_tintas_litros != 0:
    quantidade_galoes_mistura += 1
preco_mistura = (quantidade_latas_mistura * valor_da_lata_tinta_reais) + (quantidade_galoes_mistura * valor_galao_de_tinta_reais)
print(f"Você irá comprar {quantidade_latas_mistura} latas de 18 litros e {quantidade_galoes_mistura} galões de 3,6 litros, e custará {preco_mistura:.2f} reais.")


