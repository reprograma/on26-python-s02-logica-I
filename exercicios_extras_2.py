# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 

import math

raio = input("Informe o raio do círculo: ")

π = math.pi

area = π * float(raio) ** 2

print("A área do círculo é: ", area)

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

lado = float(input("Informe o lado do quadrado: "))

area = lado * 2

print("O dobro da área é igual a ", (area*2))

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

remuneracao_hora = float(input("Informe a remuneração por hora: "))
horas_trabalhadas_mes = float(input("Informe o número de horas trabalhadas no mês: "))

salario = remuneracao_hora * horas_trabalhadas_mes

print("O salário é igual a ", salario, " reais")

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9). 

temperatura_fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

temperatura_celcius = 5 * ((temperatura_fahrenheit-32) / 9)

print("A temperatura em graus Celcius é: ", temperatura_celcius)

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
# °F = (°C × 9/5) + 32 

temperatura_celcius = float(input("Informe a temperatura em Celcius: "))

temperatura_fahrenheit = (temperatura_celcius * 1.8) + 32

print("A temperatura em graus Fahrenheit é: ", temperatura_fahrenheit)