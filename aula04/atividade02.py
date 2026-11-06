vendas = float(input('Valor da venda: '))
salario = float(input('Valor do salário: '))

if vendas >= 1000:
    bonus = 150.00
    total = bonus + salario
    print(f'Você ganhou um bônus de R$ {bonus:.2f}. \nSalário de R$ {salario:.2f}. \nEste mês você receberá o valor total de R$ {total}')
elif vendas >= 500:
    bonus = 75.00
    total = bonus + salario
    print(f'Você ganhou um bônus de R$ {bonus:.2f}. \nSalário de R$ {salario:.2f}. \nEste mês você receberá o valor total de R$ {total}')
else: 
    print(f'Este mês não temos bônus para somar. Seu salário será de R$ {salario:.2f}. \nTente na próxima!')
    