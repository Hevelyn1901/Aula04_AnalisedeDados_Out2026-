valor_compra = float(input('Informe qual foi o valor da compra: '))

if valor_compra > 250:
    desconto = valor_compra * 0.16
    total_compra = valor_compra - desconto
    print(f'O valor total da sua compra com desconto ficou em R$ {total_compra:.2f}. Obrigada, volte sempre!')
else:
    print(f'O valor total da sua compra ficou em R$ {valor_compra:.2f}. Obrigada, volte sempre!')


    