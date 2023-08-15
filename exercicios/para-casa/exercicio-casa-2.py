area_total = float(input("Área a ser pintada em m²: "))

latas = round(((area_total/3)/18) + 0.5)

custo = latas*80


print("O número de latas necessário para pintar é:", latas)
print("O valor a pagar é", custo)

    




