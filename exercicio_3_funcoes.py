# Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.
print ("Calcule o valor total de 3 boletos seus!")
print ("Digite o valor do primeiro boleto: ")
valor1 = float(input())
print ("Digite o valor do segundo boleto: ")
valor2 = float (input())
print ("Digite o valor do terceiro boleto: ")
valor3 = float (input())

def somaBoletos(p1, p2, p3):
    soma = (valor1 + valor2 + valor3)
    return soma
print ("O valor total que você irá pagar é: ", somaBoletos(valor1,valor2,valor3))
   
    