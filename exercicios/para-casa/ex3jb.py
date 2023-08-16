#Faça um programa, com uma função que necessite de três argumentos, 
#e que forneça a soma desses três argumentos.

def sacolao(laranja, pera, pessego):
    total_frutas = (laranja + pera + pessego)
    return total_frutas
  
laranja = 3
pera = 5
pessego = 2

total_frutas = sacolao(laranja, pera, pessego)
print("Unidades de frutas compradas: ", total_frutas)
    

