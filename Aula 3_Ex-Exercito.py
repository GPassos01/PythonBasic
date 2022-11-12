#programa q pergunta a idade, peso e altura de uma pessoa e decide se esta apta a entrar no exercito.
#Para entrar é preciso ter maisou igual de 18 anos, pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70 metros


idade = int(input('Idade do candidato: '))
peso = int(input('Peso do candidato (em quilogramas): '))
altura = float(input('Altura do candidato (em metros): '))
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Candidato Apto')
else:
    print('Candidato não Apto')
