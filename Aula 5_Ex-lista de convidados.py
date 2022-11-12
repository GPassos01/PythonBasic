'''
Faça um programa que pergunte a quantidade de pessoas que
serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Depos irá imprimir todos os nomes da lista.
'''

numero_de_convidados = input('Coloque a quantidade de convidados: ')
lista = 1
nomes = []
while lista <= int(numero_de_convidados):
    nomes.append(input('Nome do convidado: '))
    lista += 1
    if lista > int(numero_de_convidados):
        break
print('\n\t LISTA DE CONVIDADOS \n ')
numero = 0
for n in nomes:
    numero += 1
    print('Convidado', str(numero) + ':',n)
