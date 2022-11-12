'''
Escreva uma função que receba um objeto de coleção(lista,tupla,conjunto)
e retorna o valor do maior numero dentro dessa coleção.
Faça outra função que retorna o menor valor dessa coleção.
'''


def maior_numero(coleçao):
    maior_item = coleçao[0]
    for item in coleçao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor_numero(coleçao):
    menor_item = coleçao[0]
    for item in coleçao:
        if item < menor_item:
            menor_item = item
    return menor_item

print('O maior numero é:', maior_numero([1,2,3,54,2,3,87,3]))
print('O menor numero é:', menor_numero([1,2,3,54,2,3,87,3]))



     
