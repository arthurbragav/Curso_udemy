"""
Listas

Listas em Python funcionam como vetores/matrizes/arrays
com a diferença de serem DINÂMICOS e também podermos colocar
QUALQUER tipo de dado

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nessas linguagens, se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Pyhton:
 - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
 - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes [];

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))  # Cria uma lista com números de 0 a 10;

lista5 = list('Geek University')  # Cria uma lista igual a lista2;

#  Podemos facilmente checar se determinado valor está contido na lista
num = 0
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#  Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista;
print(lista1.count(1))
print(lista5.count('e'))

#  Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append
Obs: Com append nós só conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) #  Isso é possível pois foi adicionado uma lista, que é um tipo de dado
print(lista1)


if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  #  Nesse caso os itens são adicionados individualmente, e não em conjunto como no append
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do índice
# Isso não substitui o valor inicial. Ele será descoado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)


#  Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#  Outra forma de inverter

print(lista1[::-1])  #  Slice de string, nesse caso começa na posição 0 e vai até o final, por isso está ::
print(lista2[::-1])

#  Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#  Podemos contar quantos elementos existem dentro da lista
print(len(lista5))


#  Podemos remover um elemento pelo índice
#  Os elementos à direita deste índice serão deslocados para a esquerda
#  Se não houver elemento no índice informado, teremos o erro index error
lista5.pop(2)
print(lista5)

#  Podemos remover facilmente o último elemento da lista
#  O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

#  Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

#  Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#  Podemos facilmente converter uma string para uma lista

#  Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#  o Split, por padrão, separa os elementos da lista pelo espaço entre elas

#  Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # Nesse caso, informamos ao split que o separador é a vírgula, e não o espaço como no exemplo anterior
print(curso)

#  Convertendo uma lista em string
lista6 = ['Programação', 'em', 'Pyhton:', 'Essencial']
print(lista6)
#  Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string;
curso = ' '.join(lista6)
print(curso)
#  Abaixo estamos falando: pega a lista6, coloca $ entre cada elemento e transforma em uma string;
curso = '$'.join(lista6)
print(curso)

#Iterando sobre listas

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])# verde
print(cores[1])# amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como uma roda, onde o final de um elemento está ligado ao início da lista
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print(cores[-5]) # Erro,pois não existe esse índice

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

    # Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

    # Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes, mas úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual índice da lista está o valor 6?
print(numeros.index(6))
# Em qual índice da lista está o valor 9?
print(numeros.index(9))

#OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# print(numeros.index(19))
# OBS: Sempre retorna o índice apenas do primeiro elemento encontrado, se tiver outro, não será mostrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar, nesse caso a partir do índice 1
print(numeros.index(5, 1))

# Podemos fazer busca dentro de um range, início/fim
print(numeros.index(8, 3, 6)) # Buscar o índice de valor 8, entre os índices 3 a 6



# Revisão de slicing

# lista[inicio:fim:passo]
# range (inicio:fim:passo)

# Trabalhando com slice de listas com o parâmetro 'início'
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de listas com o parâmetro 'fim'
print(lista[:2]) # Começa em 0 e pega até o índice 2 - 1

print(lista[:4]) # Começa em 0 e pega até o índice 4 - 1

print(lista[1:3]) # Começa em 1 e pega até o índice 3 - 1

# Trabalhando com slice de listas com o parâmetro 'passo'
print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

#  Soma* , Valor máximo*, Valor mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # valor máximo
print(min(lista))  # valor mínimo
print(len(lista))  # tamanho da lista


#  Transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


#  Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

#  OBS: Se tivermos um número diferente de elementos ou variáveis para receber os dados, teremos ValueError


#  Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que, ao utilizarmos lista.copy, copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente independentes
# Ou seja, modificando uma, não afeta a outra. Isso em Python é chamado de Deep Copy, ou Cópia Profunda.

# Forma 2 - Shallow Copy

lista = [1, 2, 3]

print(lista)

nova = lista #cópia

print(nova)

nova.append(4)
print(lista)
print(nova)

#  Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar a modificação
# em uma das listas, essas modificação se refletiu em ambas as listas. Isso em Python é chamado Shallow Copy
"""
