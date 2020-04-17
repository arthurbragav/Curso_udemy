"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for satisfeita

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplos:

num = 5
num < 5 --> False
num < 10 --> True

Em um loop while é importante que cuidemos do critério de parada para não ter loop infinito indesejado

Não tem "do while" em Python

Para atualização de tela em jogos, usa-se um loop infinito

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1
"""
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jessica?')
