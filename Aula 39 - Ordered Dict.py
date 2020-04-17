"""
Módulo Collections - Ordered Dict

# Em um dicionário, a ordem de inserção dos alementos não é GARANTIDA
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')


# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor = {valor}')

# Dessa forma, ele mantém a ordem
"""
# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True ou False --> True, já que a ordem não importa no dicionário comum

# Ordered Dict

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False, já que a ordem dos elementos importa no OrderedDict




