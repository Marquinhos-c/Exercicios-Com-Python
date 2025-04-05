# soma da diagonal principal
def soma_diagonal_principal(matriz):
    soma = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                soma += matriz[i][j]
    return soma

dimensao_matriz_n = int(input('Digite a dimenção da matriz: '))
matriz = []

for i in range(dimensao_matriz_n):
    coluna = []
    for j in range(dimensao_matriz_n):
        numero = int(input('Digite um número: '))
        coluna.append(numero)
    matriz.append(coluna)

resultado_soma_diagonal_principal = soma_diagonal_principal(matriz)
# mostrando resultado da soma
print(f'Soma da diagonal principal: {resultado_soma_diagonal_principal}')
# verificando se a soma é par ou impar
if resultado_soma_diagonal_principal % 2 == 0:
  print("A soma dos elementos da diagonal principal é par.")
else:
  print("A soma dos elementos da diagonal principal é ímpar.")


#função para calcular media nas posições
def calcular_media(notas):
  return round((notas[0]+notas[1])/2,2)

quantidade_de_alunos = int(input('Informe a quantidade de alunos: '))
lista_nomes = []
matriz_notas = []
# coletando nomes e notas do aluno e adicionando nas listas
for i in range(quantidade_de_alunos):
  nome = input('Informe o nome do aluno: ')
  lista_nomes.append(nome)
  lista_notas = []
  for j in range(2):
    nota = float(input(f'Informe a nota {j+1}: '))
    lista_notas.append(nota)
  matriz_notas.append(lista_notas)

# verificando se o aluno está aprovado ou reprovado
for i in range(quantidade_de_alunos):
  media = calcular_media(matriz_notas[i])
  if media >= 6:
    print(f'O aluno {lista_nomes[i]} está aprovado com a média {media}')
  else:
    print(f'O aluno {lista_nomes[i]} está reprovado com a média {media}')