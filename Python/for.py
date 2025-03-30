#tabuada
n = int(input('Quer a tabuada de qual numero? '))
for item in range(10):
    multiplicador = item + 1
    print(f'A tabuada de {n} x {multiplicador} = {(multiplicador) * n}')
    print('-'*30)