# 15. Em um concurso de miss, os jurados
# precisam digitar o nome das 16
# candidatas e suas respectivas notas (0 a
# 10). Crie um programa que leia estas
# informações e que, ao final do programa,
# apresente apenas o nome e a nota da
# vencedora
def validacaoNotas():
    nota = float(input('Informe uma nota: '))
    while((nota < 0) or (nota > 10)):
        print('Erro!!! Informe uma nota entre 0 e 10')
        nota = float(input('Informe uma nota: '))
    return nota

def miss():
    nomeVencedora = ''
    notaVencedora = 0
    for i in range(1,17):
        nome = input('Informe o nome da {}ª candidata: '.format(i))
        nota = validacaoNotas()#Números com vírgula e não negativos
        #Verificação da vencedora
        if(nota > notaVencedora):
            notaVencedora = nota
            nomeVencedora = nome
    return 'Vencedora: {}\nNota: {}'.format(nomeVencedora, notaVencedora)

