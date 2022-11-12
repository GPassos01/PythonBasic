def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp
print(soma(5,15))

def true_false(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
if true_false('Gabriel'):
    print('"Gabriel" tem 7 letras')
