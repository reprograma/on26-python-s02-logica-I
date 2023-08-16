## Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def calcular_tintas(area):
    litros_necessarios = area / 3
    latas_cheias = math.ceil(litros_necessarios / 18)
    preco_total = latas_cheias * 80
    return latas_cheias, preco_total

## Entrada do usuário

area_a_ser_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

## Cálculos

latas_cheias, preco_total = calcular_tintas(area_a_ser_pintada)

## Saída

print(f"Quantidade de latas de 18 litros a serem compradas: (latas_cheias)")
print(f"Preço total: R$ (preco_total:.2f)")