# Exercícios de Estrutura Sequencial 1-15

# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Alô, mundo!")

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 

input("O número informado foi ")

# 3. Faça um Programa que peça dois números e imprima a soma. 

numero1 = float(input())
numero2 = float(input())    
print (numero1 + numero2)

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_bimestre1 = float(input("Informe a nota do 1º bimestre: "))
nota_bimestre2 = float(input("Informe a nota do 2º bimestre: "))
nota_bimestre3 = float(input("Informe a nota do 3º bimestre: "))
nota_bimestre4 = float(input("Informe a nota do 4º bimestre: "))

media = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4)/4

print("A média é: ", media)

# 5. Faça um Programa que converta metros para centímetros.

conversao = float(input("Informe o valor em metros: ")) * 100

print("O valor em centímetros é: ", conversao)