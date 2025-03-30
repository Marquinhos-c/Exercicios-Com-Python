#exercicio 1
def soma_par_impar(n):
    soma_par = 0
    soma_impar = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            soma_par += i
        elif i % 2 == 1:
            soma_impar += i
    return soma_par, soma_impar

n = int(input('Escolha um número: '))
soma = soma_par_impar(n)
print('\n')
print(f'A soma de pares e soma impares {soma}...')


#exercicio 2
def verificar_numero_primo(numero):
    if numero % 1 and numero % numero:
        numero = True
    else:
        numero = False
    return numero

n = int(input('Digite um número: '))
primo = verificar_numero_primo(n)
print(primo)