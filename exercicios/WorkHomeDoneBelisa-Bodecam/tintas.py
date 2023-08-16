def caucular_numero_de_litros_de_tinta(numero_de_metros_quadrados, area_por_litro):
    numero_de_litros_de_tinta = numero_de_metros_quadrados / area_por_litro
    return numero_de_litros_de_tinta


metros_quadrados =  float(input("Digite o tamanho em M² de área para pintar "))
metros_quadrados_por_litro = 3
tamanho_da_lata_em_litros = 18
preco_da_lata = 80

litros = caucular_numero_de_litros_de_tinta(area_por_litro= metros_quadrados_por_litro, numero_de_metros_quadrados= metros_quadrados)
print (litros)
latas_inteiras = int(litros/tamanho_da_lata_em_litros)
if(litros%tamanho_da_lata_em_litros != 0):
    latas_inteiras += 1
    
    valor_total = latas_inteiras * preco_da_lata
print(valor_total, litros, latas_inteiras)