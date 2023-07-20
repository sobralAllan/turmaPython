from exercicio01 import dobro
from exercicio01 import triplo
from exercicio02 import reajuste
from exercicio03 import parImpar
from exercicio03 import positivoNegativoTres
from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import exercicio06
from exercicio07 import impares
from exercicio08 import somarInteiro
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio09 import somarNumero
from exercicio10 import calcularMedia
from exercicio11 import maiorMenor
from exercicio12 import positivoNegativo
from exercicio13 import fatorial
from exercicio14 import mediaVolei
from exercicio15 import miss
from exercicio16 import eleicao
def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo: ' +
          '\n0. SAIR'         +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição Vetor')

def operacao():
    opcao = 1 #Instanciar = Dar um valor inicial
    while(opcao != 0):
        # Chamar o método de cima
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))

        #Executo a ação
        if(opcao == 0):
            #Instruções do exercício 01
            print('Obrigado!')
        elif(opcao == 1):
            print('\nExercício 01')
            num = int(input('Informe um número: '))
            print('Dobro: {}\nTriplo: {}'.format(dobro(num),triplo(num)))
        elif(opcao == 2):
            print('\nExercício 02')
            salario = float(coletarPositivo())
            print('O reajuste é: R$ {}'.format(reajuste(salario)))
        elif(opcao == 3):
            print('\nExercício 03')
            num = int(input('Informe um número: '))
            print(parImpar(num))
            print(positivoNegativoTres(num))
        elif(opcao == 4):
            #Utilizar o exercício 04
            print('\nExercício 04')
            print(somarInteiro())
        elif(opcao == 5):
            #Exercício05
            print('\nExercício 05')
            num = int(input('Informe o número'))
            n = coletarPositivo()
            tabuada(num,n)
        elif(opcao == 6):
            # Exercício06
            print('\nExercício 06')
            inicio = int(input('Informe o início'))
            fim = int(input('Informe o fim'))
            exercicio06(inicio,fim)
        elif(opcao == 7):
            # Exercício07
            print('\nExercício 07')
            impares()
        elif(opcao == 8):
            # Exercício08
            print('\nExercício 08')
            print(somarInteiro())
        elif(opcao == 9):
            #Exercício 09
            print('\nExercício 09')
            print(somarNumero())
        elif(opcao == 10):
            #Exercício 10
            print('\nExercício 10')
            print(calcularMedia())
        elif(opcao == 11):
            #Exercício 11
            print('\nExercício 11')
            print(maiorMenor())
        elif(opcao == 12):
            print('\nExercício 12')
            print(positivoNegativo())
        elif(opcao == 13):
            print('\nExercício 13')
            num = int(input('Informe um número: '))
            print(fatorial(num))
        elif(opcao == 14):
            print('\nExercício 14')
            print(mediaVolei())
        elif(opcao == 15):
            print('\nExercício 15')
            print(miss())
        elif(opcao == 16):
            print('\nExercício 16')
            print(eleicao())
        elif(opcao == 17):
            return
        elif(opcao == 18):
            return
        elif(opcao == 19):
            return
        elif(opcao == 20):
            return
        elif(opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar'))
            apagarPosicao(posicao-1)
        else:
            print('Opção escolhida não é válida, digite novamente!')