#11. Escreva um algoritmo que leia valores
#inteiros e encontre o maior e o menor
#deles. Termine a leitura se o usuário
#digitar zero (0);
def maiorMenor():
    maior = 0
    menor = 0
    num = 1
    flag = False #Valor Lógico, binário
    while(num != 0):
        num = int(input('Informe um número: '))
        if(num != 0):#Evito que o zero seja relacionado
            if(flag == False):
            #Primeira vez do código, eu instancio a variável
                maior = num #Instanciei os valores maiores e menores
                menor = num
                flag = True

            #Definir o maior e menor
            if(num > maior):
                maior = num

            if(num < menor):
                menor = num

    return 'Maior: {} \n Menor: {}'.format(maior, menor)

