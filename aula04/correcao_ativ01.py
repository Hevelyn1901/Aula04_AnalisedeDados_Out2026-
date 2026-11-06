valor = float(input('Valor da compra: '))

if valor > 250:
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f'Desconto de R$ {desconto:.2f}. \nTotal a pagar: R$ {valor_final}')
else:
    print(f'Sem desconto R$ {valor:.2f}')
