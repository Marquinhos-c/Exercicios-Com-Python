#verificando idade
while True:
    idade = int(input('Digite a idade: '))
    if idade >= 0 and idade <= 12:
        print('Criança!')
        break
    elif idade >= 13 and idade <= 17:
        print('Adolescente!')
        break
    elif idade >= 18 and idade <= 59:
        print('adulto!')
        break
    elif idade >= 60:
        print('idoso!')
        break
    else:
        print('idade invalida:')
        break    


# mostrando quantos dias falta pra vencer
flag = True
indice = 0
lista_vencimento = [5,12,4,7,9,33]

while flag == True:
    print(f'A quantidade de dias para o vencimento do produto - {lista_vencimento[indice]}')
    indice += 1

    if indice == len(lista_vencimento):
        flag = False