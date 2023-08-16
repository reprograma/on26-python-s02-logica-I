 
 #Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
 #Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
 #Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
 
 
tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_tinta = tamanho_area / 3

#código utilizando quociente, para arredondar a quanqtidade de latas de tinta
latas_tinta = (litros_tinta + 17) // 18

preco_total = latas_tinta * 80

# Resultado exibido ao usuário
print(f"Você precisará de {latas_tinta} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}")