#exercicio em sala


def calcula_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)
    return media

nota1 = 8.5
nota2 = 6.7
nota3 = 4.5
peso1, peso2, peso3 = float(input()), float(input()), float(input())


print(calcula_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3))

