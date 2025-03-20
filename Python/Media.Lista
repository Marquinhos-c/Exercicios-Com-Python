# Aprovação -> média -> 7
# Recuperação -> média >= 5 e média < 7
# Reprovação caso contrario

notas = [] 

for i in range(4):
    notas.append(float(input(f'Insira a nota {i+1}: ')))

soma = 0
for i in range(4):
    soma += notas[i]

media = soma/4

if media >= 7:
    print('Aprovado! ')
elif media >= 5 and media < 7:
    print('Recuperação! ')
else:
    print('Reprovado! ')