# 12. Escreva um algoritmo que leia 20
# valores inteiros e ao final exiba:
# A) a soma dos números positivos;
# B) a quantidade de valores negativos
def positivoNegativo():
    soma = 0
    contarNegativo = 0
    for i in range(20):
        num = int(input('{}º número: '.format(i+1)))
        #a. soma dos positivos
        if(num > 0):
            soma += num
        #b. contando os negativos
        elif(num < 0):
            contarNegativo += 1
    return 'Somar Positivos: {} \nContar Negativos: {}'.format(soma,contarNegativo)