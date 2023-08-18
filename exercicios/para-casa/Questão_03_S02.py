# Exercício 3
## Link de acesso: https://wiki.python.org.br/ExerciciosFuncoes

### Enunciado: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def nota_final (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)


nota1 = int(input ("Digite a nota 1"))

nota2 = int(input ("Digite a nota 2"))

nota3 = int(input ("Digite a nota 3"))

print ("A nota final é",nota_final(nota1,nota2,nota3))