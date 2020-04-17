"""
[1] - Utilize Camel Casepara nome de classes;
class Calculadora
class CalculadoraCientifica

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;
def soma()
def soma_dois()
numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação! (Não use TAB)
if 'a' in 'banana":
    print ('tem')

[4] - Linhas em branco
-Separar funções e definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco;


class Classe
    pass


class Outra
    pass

[5] - Imports
- Imports devem ser sempre em linhas separadas

# Import Errado
import sys, os

# Import certo
import sys
import os

# Não há problemas em utilizar (não é pacote completo)
from types impor StringType, ListType

# Caso tenha muitos imports de um mesmo pacite, recomenda-se fazer:
from types import (
    StringType,
    ListType
    SetType
    OutroType
)

- Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis globais;

[6] - Espaços em expressões e instruções
# Não faça:
funcao ( algo[ 1], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:
algo(1)

# Não faça:
dict ['chave' ] = lista [indice]

# Faça:
dict['chave' = lista[indice]

# Não faça:
x              = 1
y              = 3
variavel_longa = 5

#Faça:
x = 1
y = 3
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha;

"""