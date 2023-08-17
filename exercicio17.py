# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 m² 
# e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.
# O Programa deve considerar misturar latas e galões, 
# de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, 
# isto é, considere latas cheias.

print ("Digite quantos metros quadrados você vai pintar: ")
inf_metros_quadrados = float (input())
litros = inf_metros_quadrados/6
qtd_latas = int (litros /18.0)
qtd_galao = int ((litros - qtd_latas *18) /3.6)

if litros - qtd_galao * 18 % 3.6 == 0:
        mistura_galao += 1


print("Quantidade de latas: ", qtd_latas) 
print ("Quantidade galões: ",  qtd_galao) 
print ("Valor Total latas e galões R$: ", float (qtd_latas * 80) + (qtd_galao * 25))
