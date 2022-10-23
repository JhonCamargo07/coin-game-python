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


def get_winner(option_user, full_value_bet, value_to_bet, games_played):
    data = {}
    side = get_side_random()
    print(f'\nEl ganador es: {side}')
    data.setdefault('ending_balance', value_to_bet)
    if option_user == side:
        print(' Ganaste '.upper().center(17, '*'))
        if full_value_bet < 0:
            data.setdefault('current_value', full_value_bet + value_to_bet)
        else:
            data.setdefault('current_value', (value_to_bet * 2))
        data.setdefault('is_winner', True)
    else:
        print(' Perdiste '.upper().center(18, '-'))
        data.setdefault('current_value', full_value_bet - value_to_bet)
        data.setdefault('is_winner', False)
    data.setdefault('total_games', games_played + 1)
    print()
    return data


if __name__ == '__main__':
    for data in range(1):
        print(get_winner(option_user='CARA', full_value_bet=0, value_to_bet=1000, games_played=0))
