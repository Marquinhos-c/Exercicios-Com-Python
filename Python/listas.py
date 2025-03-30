#média do aluno
notas = []
soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota) #adicionando a nota na lista
    soma += nota
media = soma / len(notas)
print(f"A média das notas é: {media}")

if media >= 6:
    print('Aluno aprovado! ')
elif media < 6:
    print('Reprovado! ')
    

#matriz e vetor
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#mostrando matriz
for linha in matriz:
    print(linha)
print('\n')

#localizando numeros da matriz
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
print('\n')

#verificando a posição do número na matriz
print(matriz[1][2])
print('\n')

#trocando o número na posição
for linha in matriz:
    matriz[2][1] = 24
    print(linha)
print('\n')