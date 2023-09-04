variavel_nova = 2

def calcula_media_poderada(nota1, nota2, peso1, peso2, nota3=None, peso3=None):
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)
    return media

x = 1
y = 2
z = 3 
peso1 = 4
peso2 = 5
peso3 = 6

retorno_da_funcao = calcula_media_poderada(nota1= x, nota2= 98, \
                                           nota3 = z, peso1=  peso1, peso2 =peso2, peso3 = peso3)
print(retorno_da_funcao)


x = 7
y = 8
z = 9 
peso1 = 4
peso2 = 5
peso3 = 6

retorno_da_funcao = calcula_media_poderada(nota1= x, nota2= 98, \
                                           nota3 = z, peso1=  peso1, peso2 =peso2, peso3 = peso3)


print(retorno_da_funcao)
#print(calcula_media_poderada(nota1, nota2, nota3, peso1, peso2, peso3))
