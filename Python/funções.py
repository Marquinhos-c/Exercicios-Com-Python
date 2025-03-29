#criando uma função
def boas_vindas(nome):
    print(f'Olá, Seja bem vindo(a) {nome}! \n')

nome = str(input('Qual é o seu nome? '))
boas_vindas(nome) #chamando a função
print(boas_vindas) #mostrando retorno


#somando dois valores e retornando resultado
def soma_dois_valores(n1, n2):
    soma = n1 + n2
    return soma

x1 = 7
x2 = 5
x3 = soma_dois_valores(x1, x2) # passando como paramentro n1 -> x1 e n2 -> x2 
print(x3)



''' #lista de produtos, vamos padronizar.
produtos = ['ABC12', 'abd012', ' ABS111', 'abB222']
texto = 'abd012'
texto = texto.upper() # colocando texte em maiusculo
texto = texto.strip() # retirando os espaços que tem no testo
print(texto) '''

#criando uma função para padronizar o testo da lisra
produtos = ['ABC12', 'abd012', ' ABS111', 'abB222']
def padronizar_texto(texto):
    texto = texto.upper() 
    texto = texto.strip() 
    return texto

for i, produto in enumerate(produtos):#acessando cada produto de produtos
    produtos[i] = padronizar_texto(produto)# chamando função para posição

print(produtos)



#Distância entre dois pontos
import math
def calcular_distancia_entre_pontos(x1, y1, x2, y2): 
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)) #usando o math.sqrt para calcular raiz quadrada da função
    return round(distancia,2)

x1 = 4.5
y1 = 6.7
x2 = 9.9
y2 = 10
distancia = calcular_distancia_entre_pontos(x1, y1, x2, y2)
print(f'A distância entre os dois pontos é {distancia}:')



# Funções dentro de funções
#função para calcular quadrilatero
def calcular_area_quadrilatero(base, altura): 
    area = base * altura
    return round(area, 2)

#função para calcular triangulo
def calcular_area_triangulo(base, altura):
    area = base * altura / 2
    return round(area, 2)
# função para escolher qual figura vai ser calculada
def calcular_area(figura_geometrica, base, altura):
    if figura_geometrica == 'quadrilatero':
        area = calcular_area_quadrilatero(base, altura)
    elif figura_geometrica == 'triangulo':
        area = calcular_area_triangulo(base, altura)
    else:
        area = 0
        print('Erro...')
    return round(area, 2)

# solicitando o usuario a forma geometrica e os valores de base e altura
figura_geometrica = str(input('Qual figura geometrica você quer a area? '))
base = float(input('Qual é a base? '))
altura = float(input('Qual é a altura? '))
Ar = calcular_area(figura_geometrica, base, altura) #chamando a função escolha
print(f'A area de {figura_geometrica} é igual a {Ar}')  