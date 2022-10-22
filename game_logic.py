import random


def get_side_random():
    NUM_MAX_RANDOM = random.randint(3, 20)

    heads_tails = []

    for side in range(NUM_MAX_RANDOM):
        if side % 2 == 0:
            heads_tails.append('CARA')
            heads_tails.append('SELLO')
            continue
        heads_tails.append('SELLO')
        heads_tails.append('CARA')

    return random.choice(heads_tails)


def get_winner(option_user, value_to_bet):
    side = get_side_random()
    print(f'Ha caido: {side}')
    if option_user == side:
        print('Ganaste')
    else:
        print('perdiste')


if __name__ == '__main__':
    for data in range(30):
        get_winner('CARA', 1000)
