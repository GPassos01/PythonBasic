var_verdade = True
print(type(var_verdade))

if var_verdade == True:
    print('var_verdade é verdadeiro')
numero_1 = int(input('numero1'))
numero_2 = int(input('numero2'))
if numero_1 > numero_2:
    print('numero1 maior que numero2')
elif numero_1 < numero_2:
    print('numero2 maior que numero1')
elif numero_1 == numero_2 and numero_1 == '1':
    print('numero 1 e 2 sao iguais a 1')
else:
    print('numero 1 e 2 sao iguais e diferentes de 1')
