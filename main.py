games_played = 0


def game_start():
    try:
        print_welcome()
        get_option()
    except Exception as e:
        print(f'Ocurri\u00f3 un error: {e}')


def print_welcome():
    welcome = 'Bienvenido a cara o sello'
    print(f' {welcome} '.center(len(welcome) + 50, '='))
    print(f'\u00bfCrees poder ganarle al destino? ... Prob\u00e9moslo')


def get_option():
    print()
    print('Elige tu primero \u00bfcara o sello?')
    option_user = input('Escribe "cara" o "sello": ').upper()
    if option_user != 'CARA' and option_user != 'SELLO':
        print('Cometiste un error, intentalo nuevamente...')
        return get_option()
    print('\u00bfBuena elecci\u00f3n? Pronto lo sabremos')
    get_value_to_bet()


def get_value_to_bet():
    print()
    value_to_bet = input('Ingresa el valor a apostar: ')

    if not value_to_bet.isnumeric() or int(value_to_bet) <= 0:
        print('Valor incorrecto, por favor...')
        return get_value_to_bet()
    return int(value_to_bet)


if __name__ == '__main__':
    game_start()
