pontuacao_jogador = int(input('Informe qual foi a pontuação: '))

if pontuacao_jogador >= 100:
    pontuacao_jogador = pontuacao_jogador + 10
    print(f'Excelente! Você está com {pontuacao_jogador} pontos agora! ')
elif pontuacao_jogador >= 50:
    pontuacao_jogador = pontuacao_jogador + 5
    print(f'Parabéns! Você está com {pontuacao_jogador} pontos agora!')
else:
    print(f'Bom desempenho! Você está com {pontuacao_jogador} pontos agora! Teremos novas chances. Não desanime!')