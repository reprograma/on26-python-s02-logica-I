# Vamos pensar num exemplo.
# Imagine que você é um professor e deve calcular a média das notas dos alunos em três provas.
# Para facilitar, você qyer escrever um código que calcule as notas para você
# Vamos criar uma função para isso e nós só precisamos chamar essa função com as notas dos alunos!

def calcula_media (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

nota1 = 15
nota2 = float (input ())
nota3 = float (input ())

media = calcula_media (nota1, nota2, nota3)
print (media)