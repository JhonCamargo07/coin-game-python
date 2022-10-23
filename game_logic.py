import random


def get_side_random():
    NUM_MAX_RANDOM = random.randint(3, 20)

    heads_tails = []

    for side in range(NUM_MAX_RANDOM):
        side = random.randint(2, 100)
        if side % 2 == 0:
            heads_tails.append('CARA')
            heads_tails.append('SELLO')
            continue
        heads_tails.append('SELLO')
        heads_tails.append('CARA')
    random.shuffle(heads_tails)
    return random.choice(heads_tails)


def get_winner(data_departure):
    game_data = {}
    side = get_side_random()
    print(f'\nEl ganador es: {side}')
    game_data.setdefault('ending_balance', data_departure['value_to_bet'])

    if data_departure['option_user'] == side:
        print(' Ganaste '.upper().center(17, '*'))
        if data_departure['full_value_bet'] < 0:
            game_data.setdefault('current_value', data_departure['full_value_bet'] + data_departure['value_to_bet'])
        else:
            game_data.setdefault('current_value', (data_departure['value_to_bet'] * 2))
        game_data.setdefault('is_winner', True)

    else:
        print(' Perdiste '.upper().center(18, '-'))
        game_data.setdefault('current_value', data_departure['full_value_bet'] - data_departure['value_to_bet'])
        game_data.setdefault('is_winner', False)
    game_data.setdefault('total_games', data_departure['games_played'] + 1)

    print()
    return game_data


if __name__ == '__main__':
    for data in range(100):
        print(get_winner({'option_user': 'CARA', 'full_value_bet': 0, 'value_to_bet': 1000, 'games_played': 0}))
