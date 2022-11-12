import sys
argumentos = sys.argv

def sub(n1, n2):
  return n1 - n2
if argumentos[0] == 'sub':
  resp = sub(float(argumentos[1]), float(argumentos[2]))
  print(resp)
