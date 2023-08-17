# 16. Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. 
# Considere que a cobertura da tinta é 
# de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas 
# e o preço total.
print ("Digite quantos metros quadrados você vai pintar: ")
inf_metros_quadrados = float (input())
precoAPagar = qtd_latas = inf_metros_quadrados // 54 *80
print ("A quantidade de Latas que você deve comprar é: ", inf_metros_quadrados // 54)
print ("O Valor que você vai pagar é: ", precoAPagar)