objetos = ['livro', 'fones', 'controle', 'estojo', 'lapis', 'cofre']

for Ob in range(4):
    print(objetos[Ob])
    objetos.append('Outro Objeto')
print(objetos)

objetos2 = objetos[0:3]
print(objetos2)
numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
    
