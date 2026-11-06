valor_compra = float(input('Informe qual foi o valor da compra: '))
fidelidade = input('Programa de Fidelidade? [S/N] ').lower()[0]

if valor_compra > 100 or fidelidade == 's' :
    print('Parabéns! Você recebeu um brinde')
else:
    print('Sem brinde')