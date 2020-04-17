"""
Módulo Collections - Counter (Contador)

Collections -> High Performance Container Datetypes


Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo collections counter, que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
da ocorrência desse elemento.


# Realizando o import

from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 65, 66, 43, 34]


# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 2: 4, 3: 4, 4: 3, 5: 3, 45: 2, 65: 1, 66: 1, 43: 1, 34: 1})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


# Exemplo 3

texto =
A vitamina D e seus pró-hormônios têm sido alvo de um número crescente de pesquisas nos
últimos anos, demonstrando sua
função além do metabolismo do cálcio e da formação óssea,
incluindo sua interação com o sistema imunológico, o que
não é uma surpresa, tendo em vista a expressão do receptor de
vitamina D em uma ampla variedade de tecidos corporais como
cérebro, coração, pele, intestino, gônadas, próstata, mamas
e células imunológicas, além de ossos, rins e paratireoides.1
Estudos atuais têm relacionado a deficiência de vitamina
D com várias doenças autoimunes, incluindo diabetes melito
insulino-dependente (DMID), esclerose múltipla (EM), doença
inflamatória intestinal (DII), lúpus eritematoso sistêmico (LES)
e artrite reumatoide (AR).1-4 Diante dessas associações, sugere-
-se que a vitamina D seja um fator extrínseco capaz de afetar
a prevalência de doenças autoimunes.5
A vitamina D parece interagir com o sistema imunológico
através de sua ação sobre a regulação e a diferenciação de células como linfócitos,
macrófagos e células natural killer (NK),
além de interferir na produção de citocinas in vivo e in vitro.


palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

print(res.most_common(10))
"""



