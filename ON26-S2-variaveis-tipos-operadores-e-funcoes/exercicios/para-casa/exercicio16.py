# exercicio 16
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
tamanho_metros = float(input()) # o espaço em m2 que irei pintar
qtd_litro = tamanho_metros / 3 # quantidade de litro de tinta que eu vou precisar
litro18 = qtd_litro / 18 # quantas latas de 18l eu vou precisar?
custo = litro18 * 80 # quanto vai custar?
lata = 18
preco = 80
print(qtd_litro)
print(litro18)
print(custo)