# Atividade 1:
#somando pares e impares
def soma_par_impar(n):
  soma_pares = 0
  soma_impares = 0
  for i in range(1, n+1):
    if i % 2 == 0:
      soma_pares += i
    else:
      soma_impares += i
  return soma_pares, soma_impares

n = int(input("Digite um número inteiro: "))
soma_pares, soma_impares = soma_par_impar(n)
print("A soma dos números pares de 1 a", n, "é:", soma_pares)
print("A soma dos números impares de 1 a", n, "é:", soma_impares)


# Atividade 2
# verificando se o número é primo
def varificar_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

n = int(input("Digite um número: "))
varificar_numero_primo(n)


# Atividade:
#calculando fatorial
def calcular_fatorial(n):
  contador = 1
  fatorial = 1
  while contador <= n:
    fatorial *= contador
    contador += 1
  return fatorial

n = int(input("Digite um número: "))
f = calcular_fatorial(n)
print(f'{n}! = {f}')


# Atividade 4:
#média da lista, maior número e menor
def analisa_numeros(lista_numeros):
  for i in enumerate(lista_numeros):
    media = sum(lista_numeros)/len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    return print(f'O menor número digitado é: {menor}', f'O maior número digitado é: {maior}', f'A média dos números digitados é: {media}')


digitos = int(input('Quantos números você quer digitar? '))
lista_numeros = []
for i in range(digitos):
  numeros = int(input('Digite um número: '))
  lista_numeros.append(numeros)

analisa_numeros(lista_numeros)


# Atividade 5:
#fazendo o usuario tentar acerta  o numero
import random
def jogo_adivinhacao(tentativas):
  for i in range(tentativas):
    sorteio = random.randint(1, 100)
    chute = int(input('Chute um número: '))
    if chute > sorteio:
      print(f'Chute alto, número era {sorteio}: ')
    elif chute < sorteio:
      print(f'Chute baixo, número era {sorteio}: ')
    else:
      if chute == sorteio:
        print('Parabéns, você acertou!')

tentativa = int(input('Quer tentar quantas vezes? '))
jogo_adivinhacao(tentativa)