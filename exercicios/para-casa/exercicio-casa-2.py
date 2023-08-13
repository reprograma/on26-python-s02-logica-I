area_total = float(input("Área a ser pintada em m²: "))

a = (area_total/3)/18

latas = round(a + 0.5)

def valor_a_pagar(area_total, a, latas):
    custo = latas*80
    return custo

print("O número de latas necessário para pintar é:", latas)
print("O valor a pagar é", valor_a_pagar(area_total, a, latas))

    




