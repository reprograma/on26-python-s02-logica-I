#Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#l.)comprar apenas latas de 18 litros;
#2.) comprar apenas galões de 3,6 litros;
#3.) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

metros_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = metros_quadrados / 6

litros_por_lata = 18
litros_por_galao = 3.6

latas_necessarias = int(litros_necessarios / litros_por_lata)
galoes_necessarios = int(litros_necessarios / litros_por_galao)

# Preços totais para cada opção
preco_lata = 80
preco_galao = 25

preco_total_latas = latas_necessarias * preco_lata
preco_total_galoes = galoes_necessarios * preco_galao

# Exibir os resultados ao usuário
print(f"Quantidade de tinta necessária: {litros_necessarios:.2f} litros")
print(f"Opção 1 - Comprar apenas latas: {latas_necessarias} latas - Preço: R$ {preco_total_latas:.2f}")
print(f"Opção 2 - Comprar apenas galões: {galoes_necessarios} galões - Preço: R$ {preco_total_galoes:.2f}")