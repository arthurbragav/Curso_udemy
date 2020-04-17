"""
Estruturas condicionais
if, else, elif

Estrutura condicional if, else em C

if(idade < 18){
    printf("Menor de idade");
}else{
    printf("Maior de idade");
}


Estrutura condicional if, else em Java

if(idade<18){
    System.out.println("Menor de idade");
}else{
    System.out.println("Maior de idade");
}
"""

idade = 26

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
