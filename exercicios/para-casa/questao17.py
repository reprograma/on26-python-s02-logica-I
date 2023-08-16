## Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
## Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

## Função para calcular a quantidade de latas e galões necessários

def calcular_tintas(area):
    area_com_folga = area * 1.1
    litros_necessarios = area_com_folga / 6
    latas_cheias = int(litros_necessarios / 18)
    litros_restantes = litros_necessarios % 18
    galoes_necessarios = math.ceil(litros_restantes / 3.6)
    return latas_cheias, galoes_necessarios

## Função para calcular o custo total

def calcular_custo(latas_cheias, galoes_necessarios):
    custo_latas = latas_cheias * 80
    custo_galoes = galoes_necessarios * 25
    custo_total = custo_latas + custo_galoes
    return custo_total

## Entrada do usuário

area_a_ser_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

## Cálculos

latas_cheias, galoes_necessarios = calcular_tintas(area_a_ser_pintada)
custo_total = calcular_custo(latas_cheias, galoes_necessarios)

## Saída

print(f"Quantidade de latas de 18 litros: (latas_cheias)")
print(f"Quantidade de galões de 3,6 litros: (galoes_necessarios)")
print(f"Custo total: R$ (custo_total:.2f)")