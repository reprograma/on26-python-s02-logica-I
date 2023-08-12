# Vamos pensar num exemplo. 
# Imagine que você é um professor e deve calcular a média das notas dos alunos em três provas.
# Para facilitar, você quer escrever um código que calcule as notas pra ti. 
# Vamos criar uma função para isso e nós só precisamos chamar essa 
# função com as notas dos alunos! 

def calcula_media(nota1, nota2, nota3=None):
    if not nota3:
        nota3 = 15
    print(nota3)
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = 15
nota2 = 98
nota4 = 19 

print(calcula_media(nota2=nota1, nota1=nota2, nota3=nota4))
