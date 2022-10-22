import random
from game_logic import get_winner

MIN_GAMES = 3
phrases_welcome = ['\u00bfCrees poder ganarle al destino? ... Prob\u00e9moslo', 'El destino hoy no est\u00e1 de tu lado \u00bfo si?', 'No hay manera de ganarme, pero intentalo...', 'Hoy puedes perder todo lo que apuestes \u00bfAun as\u00ed quieres apostar?']
phrases_option = ['\u00bfBuena elecci\u00f3n? Pronto lo sabremos', 'Tu respuesta fue r\u00e1pida \u00bfpero inteligente?', '\u00bfSeguro que era la opci\u00f3n correcta?', 'zzzz eres muy lento para elegir', 'Sabia decisi\u00f3n, ahora estoy templando']
phrases_finished = ['De acuerdo, fue un placer jugar contigo', '\u00bfTe cansaste?, espero volver a jugar contigo', 'Solo los cobardes huyen del campo de batalla']


def game_start():
    print_welcome()
    game_reload()


def game_reload():
    games_played = 0
    try:
        while games_played < MIN_GAMES:
            if games_played > 0:
                print('Vamos de nuevo, te doy otra oportunidad \u00bfla aprovechar\u00e1s?')
            get_option()
            games_played += 1
        else:
            print('\u00bfQuieres seguir jugando?')
            keep_playing = input('Escribe "si" o "no": ').upper()
            if keep_playing == 'SI':
                return game_reload()

            print()
            print(random.choice(phrases_finished))
            message_finished = 'Juego terminado'
            print(f' {message_finished} '.center(len(message_finished) + 50, '='))

    except Exception as e:
        print(f'Ocurri\u00f3 un error: {e}')


def print_welcome():
    welcome = 'Bienvenido a cara o sello'
    print(f' {welcome} '.center(len(welcome) + 50, '='))
    # print(f'{phrases_welcome[random.randrange(0, len(phrases_welcome))]}')
    print(random.choice(phrases_welcome))


def get_option():
    print()
    print('Elige tu primero \u00bfcara o sello?')
    option_user = input('Escribe "cara" o "sello": ').upper()
    if option_user != 'CARA' and option_user != 'SELLO':
        print('Cometiste un error, intentalo nuevamente...')
        return get_option()
    # print(f'{phrases_option[random.randrange(0, len(phrases_option))]}')
    print(random.choice(phrases_option))
    get_winner(option_user, get_value_to_bet())
    return


def get_value_to_bet():
    print()
    value_to_bet = input('Ingresa el valor a apostar: ')

    if not value_to_bet.isnumeric() or int(value_to_bet) <= 0:
        print('Valor incorrecto, por favor...')
        return get_value_to_bet()
    return int(value_to_bet)


game_start()
