# Para importar a biblioteca math para poder arredondar 
import math

# O 'input' cria um prompt para o usuário colocar a área a ser pintada em metros quadrados 
metro_quadrado_area_a_ser_pintada = float(input("Digite o metro quadrado da área a ser pintada: "))

# Calculando o volume necessário, '1.1' significa 110% para garantir 10% de folga
calculo_volume = metro_quadrado_area_a_ser_pintada / 6 * 1.1

# Definindo a quantidade de litros em uma lata
litros_por_lata = 18 
# Definindo a quantidade de litros em um galão
litros_por_galao = 3.6  

# Calculando a quantidade de latas necessárias para a mistura, arredondando para cima
quantidade_latas_mistura = math.floor(calculo_volume / litros_por_lata)

# Calculando o volume restante após adicionar as latas inteiras na mistura.
restante = math.ceil(calculo_volume - quantidade_latas_mistura * litros_por_lata)

# Calculando a quantidade de galões necessários para a mistura, arredondando para cima.
quantidade_galoes_mistura = math.ceil(restante / litros_por_galao)

# Calculando o preço total das latas de tinta na mistura
preco_lata = quantidade_latas_mistura * 80.00

# Calculando o preço total dos galões de tinta na mistura
preco_galao = quantidade_galoes_mistura * 25.00

# Calculando o preço total da mistura somando os preços das latas e dos galões
preco_mistura = preco_lata + preco_galao

# Imprimindo a quantidade de latas de tinta e galões de tinta necessários na mistura
print(f"Você irá precisar de {quantidade_latas_mistura} latas e {quantidade_galoes_mistura} galões de tinta para fazer uma mistura sem desperdício")

# Imprime o preço total usando o '.2f' para formatar com duas casas decimais
print(f"Preço total da mistura: R${preco_mistura:.2f}")







