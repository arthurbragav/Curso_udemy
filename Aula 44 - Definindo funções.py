"""
Definindo funções

 - Funções são pequenas partes de código que realizam tarefas específicas;
 - Pode ou não receber entrada de dados e retornar uma saída de dados;
 - Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada;

Já utilizamos várias funções desde que iniciamos esse curso:
 - print()
 - len()
 - max()
 - min()
 - count()
 - e muitas outras;

 # Exemplo de utilização de função

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados') AttributeError
# print(curso)

cores.clear()
print(cores)


 print(help(print))

 DRY - Don't Repeat Yourself - Não repita seu código

 Como definir funções?

 Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao


Onde:

nome_da_funcao -> SEMPRE com letras minúsculas, e se for composto, separadp por underline(Snake Case):
parametros_de_entrada -> Opcionais, onde, tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não
bloco_da_funcao -> Também chamado de corpo da função ou implementação. É onde ocorre o processamento da função.
Nesse bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, usamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido :, que é utilizado para definir blocos.


# Definindo a primeira função


def diz_oi():
    print('oi!')



OBS:

1. Veja que, dentro das nossas funções, podemos usar outras funções
2. Veja que nossa função só executa uma tarefa, ela só diz oi
3. Veja que esta função não recebe nenhum parâmetro de entrada
4. Veja que essa função não retorna nada


# Utilizando funções
# Chamada de execução
diz_oi()


Atenção:

Nunca esqueça de utilizar o parênteses ao executar uma função;

Exemplo:

Errado:
diz_oi

Certo:
diz_oi()

Errado:
diz_oi ()

# Exemplo 2


def cantar_parabens():
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vidas')


# for n in range(5):
#    cantar_parabens()
# Em Python podems inclusive criar variáveis do tipo de uma função e executar essa função através da variável

canta = cantar_parabens

canta()
"""

