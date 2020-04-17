"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    -Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
    - Não são indexados, o acesso é feito pela chave

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))


# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# print(paises['ru'])

# OBS: Caso tentemos fazer um acesso utilizando chave que não existe, teremos KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru')) # Usando o get, não da ValueError, apresenta None

# Outro exemplo
# Caso o get não encontre o objeto com a chave, será retornado None, e não será gerado KeyError

pais = paises.get('br')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o pais')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o pais {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises) # True
print('ru' in paises) # False
print('Estados Unidos' in paises) # False pois 'Estados Unidos' é um valor, não uma chave

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo dado, inclusive lista, tupla, dicionário, como chaves de dicionários.

# Tuplas, por exemplo, são bastante interessantes de se utilizar como chaves de dicionários, pois elas são imutáveis
localidades = {
    (35.6895, 39.8763): 'Escritório em Tókio',
    (40.5547, 74.0098): 'Escritório em Nova York',
    (37.8878, 122.8756): 'Escritório em São Paulo',
}



# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 400

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500}) é a mesma coisa

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma!
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas


# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos sempre informar a CHAVE, caso não encontre o elemento, um KeyError é informado
# OBS 2: Ao removermos um objeto, o valor dele é sempre retornado

# Forma 2
del receita['fev']

print(receita)

# OBS: Se a chave não existir, será gerado um KeyError
# OBS: Nesse caso, o valor removido não é retornado


Imagine que você tem um ecommerce, onde temos um carrinho de compras no qual adicionamos produtos

Carrinho de compras
Produto 1
        - nome;
        -quantidade;
        - preço;
    Produto 2:
        - nome;
        -quantidade;
        - preço;
        
        # 1 - Poderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto

# 3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto, podemos ter
# a certeza sobre cada informação

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() #  Deep copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 (Shallow Copy)

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print (outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O método .fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável, uma chave. E irá atribuir a essa chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

"""

