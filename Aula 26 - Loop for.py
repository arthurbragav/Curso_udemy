"""
Loop for
Loop - Estrutura de repetição
For - Uma dessas estruturas

C ou Java
for(int i=0;i<10; i++){
    //excecução do loop
}

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis
 - String
    nome = 'Geek University'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em lista
# Exemplo 1 de for (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo 2 de for (iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo 3 de for (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive
1
2
3
4
5
6
7
8
9
10 - Não


for numero in range(1, 10):
    print(numero)


Comando enumerate
((0, 'g'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ') --> gera uma tupla
 for _, letra in enumerate(nome):
    print(letra)

O _ se refere ao indice na tupla, e a letra, a ela mesma;

for indice, letra in enumerate(nome):
    print(nome[indice])
ou
for indice, letra in enumerate(nome):
    print(letra)
ou
for _, letra in enumerate(nome):
    print(letra)
ou
for valor in enumerate(nome):  -> Dessa forma ele mostra (0, 'G'), (1, 'e')...
    print(valor)


para não pular linha:
for letra in nome:
    print(letra, end='')

É possível colocar emojis
Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode

/ é um caracter de escape
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em lista
"""
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma += num
print(f'A soma é {soma}')
"""
# Emoji apaixonado
# Original U+1F60D
# Modificado U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)
