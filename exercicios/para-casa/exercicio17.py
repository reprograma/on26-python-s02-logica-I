tamanho = float(input())

litroCobertura_a_cadaMetro = 6 #DE UM LITRO A CADA SEIS METROS

#INFORMAÇÕES DAS LATAS
litroLata = 18
preçoLata = 80
preçoGalão = 25

#comprar apenas latas de 18 litros;

litrosNecessarios = tamanho/litroCobertura_a_cadaMetro
latasNecessarias = litrosNecessarios/litroLata
preçoNecessario = preçoLata * latasNecessarias
print("Latas necessárias: ") 
print(int(latasNecessarias))
print("Valor necessários: ") 
print(float(preçoNecessario))










