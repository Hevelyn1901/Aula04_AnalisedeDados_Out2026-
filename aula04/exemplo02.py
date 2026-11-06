ano_nascimento = int(input('Informe o ano de nascimento: '))

idade = 2026 - ano_nascimento

if idade >= 18:
    print('Parabéns!')
else:
    print('Que sorte! Você ainda é menor de idade.')
    