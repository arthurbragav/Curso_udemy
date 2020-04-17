"""
Estruturas lógicas and, or, not, is

Operadores unários:
    - not
Operadores binários
    - and, or, is

Regras de funcionamento
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido
Para o 'is', o valor é comparado com um segundo
"""

ativo = False
logado = False

if ativo or logado:
    print('Bem vindo, usuário!')
else:
    print('Ative sua conta')

# O sistema pergunta: o ativo é true? Se sim, imprime True, se não, False
print(ativo is True)

