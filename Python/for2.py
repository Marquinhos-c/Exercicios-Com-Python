#calculando a média do aluno.
notas = []
soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)
    soma += nota
media = soma / len(notas)
print(f"A média das notas é: {media}")

if media >= 6:
    print('Aluno aprovado! ')
elif media < 6:
    print('Reprovado! ')