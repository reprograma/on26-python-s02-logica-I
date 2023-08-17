def calcular_numero_de_litro_de_tinta(numero_de_metros_quadrados, area_por_litro):
    numero_de_litros_de_tinta = numero_de_metros_quadrados / area_por_litro
    return numero_de_litros_de_tinta


metro_quadrados = 25
metro_quadrado_por_litro = 3
tamanho_da_lata_em_litros = 18
preco_da_lata = 80

# calcular numero de litros de tinta
litros = calcular_numero_de_litro_de_tinta(area_por_litro= metro_quadrado_por_litro, \
                                           numero_de_metros_quadrados=metro_quadrados)
print(litros)

metro_quadrados = float(input())
novo_litros = calcular_numero_de_litro_de_tinta(metro_quadrados, metro_quadrado_por_litro)
print(novo_litros)


# calcular numero de latas de tinta
#numero_de_latas = ... 
#preco_final = ... * preco_da_lata