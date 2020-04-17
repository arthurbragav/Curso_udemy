"""
Ranges

Precisamos conhecer o loop for para usar o range
Precisamos conhecer o range para trabalhar melhor os loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória

Formas gerais:

range(valor_de_parada)

OBS: valor de parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor de parada não inclusive (início especificado, e passo de 1 em 1)
for num in range(1, 11):
    print (num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive (início padrão 0, e passo especificado)
for num in range(1, 10, 2):
    print(num)

# Forma 4 (Inversa)
range(valor_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive (valor_final especificado e passo especificado)
for num in range(10, 0, -1):
    print(num)
"""