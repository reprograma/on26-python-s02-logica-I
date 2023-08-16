# Semana 2 - prof Belissa curso Python - estudante Cris Pereira
# Exercicio 03 - Funções
# Ex. função que necessite de três argumentos, e que forneça a soma desses três argumentos

def soma (numero1, numero2, numero3):
    soma = numero1 + numero2 + numero3
    return soma

teste1 = input("Informe pontos do primero teste: ")
teste2 = input("Informe pontos do segundo teste: ")
teste3 = input("Informe pontos do terceiro teste: ")
print("Os pontos totais são:", soma(float(teste1), float(teste2), float(teste3)))
