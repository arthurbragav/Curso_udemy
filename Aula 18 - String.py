"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples
- Estiver entre aspas duplas
- Estiver entre aspas simples triplas
- Estiver entre aspas duplas triplas

\n serve para pular uma linha

nome = 'Angelina Jolie'
print (nome.upper()) --> ANGELINA JOLIE
print (nome.lower()) --> angelina jolie
print (nome.split()) --> Transforma em uma lista de strings ['Angelina', 'Jolie']

Quando armazenamos uma string, por trás dos panos, o programa faz uma lista com as letra, ex:
['A', 'n', 'g', 'e', 'l', 'i', 'n', 'a', ' ', 'J', 'o', 'l', 'i', 'e']
[0,    1,   2,   3,   4,   5,   6,   7,   8,   9,  10,   11,  12,  13] --> Posição
A primeira posição da lista é 0, e a última é o número de letras - 1

print(nome[0:4]) --> Ange (Slice de string)
print (nome.split()[0]) --> Angelina
print (nome.split()[1]) --> Jolie

Inverter a string
print(nome[::-1]) --> Comece do primeiro elemento, vá até o último e inverta

Substituir caracter
print(nome.replace('A', 'J')) --> Case sensitive!



"""