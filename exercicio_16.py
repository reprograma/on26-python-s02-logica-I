#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Recepcionar o cliente:
nome_cliente = input("Olá! É um prazer te ver aqui! Antes de continuarmos, qual o seu nome? ") 
print(nome_cliente + ", agradecemos a preferência! Vamos precisar de mais algumas informações para prosseguir com seu orçamento, ok?")

#Descobrir o tamanho da área a ser pintada:
metro2_informado_pelo_cliente =  input("Por favor, nos diga abaixo o tamanho (em m²) do espaço que deseja pintar: ")

#Definir a quantidade de m2 como float para poder calcular a quantidade de latas:
quantidade_m2 = float(metro2_informado_pelo_cliente)

#Quantidade de latas necessárias como float:
quantidade_latas_exata = quantidade_m2 / 54

#Quantidade de latas necessárias com o valor arredondado para cima:
quantidade_latas_arredondada = round(quantidade_latas_exata)

if quantidade_latas_arredondada < quantidade_latas_exata:
    quantidade_latas_arredondada = 1

#Preço total da compra considerando a quantidade de latas arredondada para cima:
preço_total = quantidade_latas_arredondada * 80

#Informando a quantidade necessária de latas ao cliente:
print("A quantidade de latas necessária é " + str(quantidade_latas_arredondada) + ". Note que nossas latas têm um tamanho padrão de 18 litros e cada litro de nossa tinta cobre 3m².")

print("O preço total de sua compra é de R$ " + str(preço_total) + " . Volte sempre!")
