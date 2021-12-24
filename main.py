players = [
  {
    'name': 'Matheus',
    'numbers': {1,2,3,4,5}
  },
  {
    'name': 'Samuel',
    'numbers': {6,7,8,9,10}
  }
]
lottery_numbers = {1,3,5,7,9}
qual_jogador = int(input('digite qual jogador: '))
print('o jogador {} acertou {} numeros'.format(players[qual_jogador-1]['name'],len(players[qual_jogador-1]['numbers'].intersection(lottery_numbers))))