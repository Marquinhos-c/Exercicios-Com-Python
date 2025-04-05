def calcular_area_quadrilatero(base, altura): 
    area = base * altura
    return round(area, 2)

def calcular_area_triangulo(base, altura):
    area = base * altura / 2
    return round(area, 2)

def menu():
    print('\n 0 - Encerrar \n 1 - Quadrilatero \n 2 - Triângulo \n')
    opcao = int(input('Digite a opção: '))
    return opcao

def executar():
    while True:
        opcao = menu()
        if opcao == 1:
            base = float(input('Digite a base do quadrilatero: '))
            altura = float(input('Digite a altura do quadrilatero: '))
            area = calcular_area_quadrilatero(base, altura)
            print(f'A área do quadrilatero é: {area}. \n')
        elif opcao == 2:
            base = float(input('Digite a base do triângulo: '))
            altura = float(input('Digite a altura do triângulo: '))
            area = calcular_area_triangulo(base, altura)
            print(f'A área do triâgulo é: {area}. \n')
        elif opcao == 0:
            print('\n')
            print('Encerrado, espero ter ajudado!\n')
            break
        else:
            print('\n')
            print('Opação invalida!\n')
            print('Encerrando...')
            break

executar()