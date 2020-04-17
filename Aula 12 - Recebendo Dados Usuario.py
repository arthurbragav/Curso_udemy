"""
Recendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
- Aspas duplas triplas
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()

nome = input('Qual seu nome?')

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')


# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade?'))

# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos' .format(nome, idade))


# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

# int{idade} => cast e a conversao de um tipo de daado para outro
print(f'A {nome} nasceu em {2020 - idade}')
