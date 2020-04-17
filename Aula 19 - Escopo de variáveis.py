"""
Escopo de variáveis

Dois casos de escopo

1 - Variáveis globais
	- Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa;
2 - Variáveis locais
	- Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
	  limitado ao bloco onde foi declarado.

Para declarar variáveis em Python, fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica, ou seja, ao declararmos uma variável, nós não colocamos seu tipo
esse tipo é inferido ao atribuírmos o valor. é possível fazer reatribuição, o que não é possível em C, por exemplo.

Exemplo de variável local
if numero > 10
    novo = numero + 10
    print(novo)
A variável 'novo' está declarada localmente dentro do bloco if, portanto é local.

"""