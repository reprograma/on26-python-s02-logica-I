m2_por_litro = 3
lata = 18
area_m2_lata = 18 * m2_por_litro
valor_lata = 80

#operações

print(" digite o tamanho da parede em m² a ser pintada")
litros_por_tamanho = (float(input()) ) / m2_por_litro
quant_latas_comprar = (litros_por_tamanho // lata) +1
print( "A quantidade de latas para comprar é de:" , quant_latas_comprar)

valor_compra = quant_latas_comprar * valor_lata
print( "O valor a ser pago é de: $", valor_compra)

