import random
from game_logic import get_winner

MIN_GAMES = 3
game_data = [{'ending_balance': 0, 'current_value': 0, 'is_winner': None, 'total_games': 0}]

phrases_welcome = ['\u00bfCrees poder ganarle al destino? ... Prob\u00e9moslo', 'El destino hoy no est\u00e1 de tu lado \u00bfo si?', 'No hay manera de ganarme, pero intentalo...', 'Hoy puedes perder todo lo que apuestes \u00bfAun as\u00ed quieres apostar?', 'Comprueba si hoy es tu d\u00eda de suerte']
phrases_option = ['\u00bfBuena elecci\u00f3n? Pronto lo sabremos', 'Tu respuesta fue r\u00e1pida \u00bfpero inteligente?', '\u00bfSeguro que era la opci\u00f3n correcta?', 'zzzz eres muy lento para elegir', 'Sabia decisi\u00f3n, ahora estoy temblando', 'Jajaj\u00e1 debiste escoger la otra opci\u00f3n', 'Est\u00e1 bien, yo elegir\u00e9 la otra opci\u00f3n']
phrases_continue = ['Okay, okay, vamos de nuevo', 'Tienes otra oportunidad \u00bfla aprovechar\u00e1s?', 'De acuerdo, continuemos', 'Despu\u00e9s del resultado como te sientes \u00bfListo para la siguiente?', 'Estoy at\u00f3nito por saber que pasar\u00e1']
phrases_finished = ['De acuerdo, fue un placer jugar contigo', '\u00bfTe cansaste?, espero volver a jugar contigo', 'Solo los cobardes huyen del campo de batalla', 'Jugaste bien baquero', 'Bien hecho guerrero, el valhalla te espera']


def game_start():
    print_welcome()
    game_reload()


def print_welcome():
    welcome = 'Bienvenido a cara o sello'
    print(f' {welcome} '.center(len(welcome) + 50, '='))
    print(random.choice(phrases_welcome))


def game_reload():
    games_played = 0
    try:
        while games_played < MIN_GAMES:
            if games_played > 0:
                print(random.choice(phrases_continue))
            get_option()
            games_played += 1
        else:
            print('\u00bfQuieres seguir jugando?')
            keep_playing = input('Escribe "si" o "no": ').upper()
            if keep_playing == 'SI':
                return game_reload()

            print()
            total_games_wom = 0
            ending_balance = game_data[-1]

            for data in game_data:
                if data['is_winner'] != None:
                    print(f'Juego #{data["total_games"]}\n\tGan\u00f3: {data["is_winner"]}\n\tSaldo inicial: {data["ending_balance"]}\n\tSaldo final: {data["current_value"]}')
                    if data['is_winner']:
                        total_games_wom += 1

            print(f'\nTotal juegos ganados {total_games_wom}/{len(game_data)-1}')
            print(f'Saldo final: {ending_balance["current_value"]}')

            print(f'\n{random.choice(phrases_finished)}')
            message_finished = 'Juego terminado'
            print(f' {message_finished} '.center(len(message_finished) + 50, '='))

    except Exception as e:
        print(f'Ocurri\u00f3 un error: {e}')


def get_option():
    print()
    print('Elige tu primero \u00bfcara o sello?')

    option_user = input('Escribe "cara" o "sello": ').upper()
    if option_user != 'CARA' and option_user != 'SELLO':
        print('Cometiste un error, intentalo nuevamente...')
        return get_option()

    print(random.choice(phrases_option))

    full_value_bet = game_data[-1]
    len_game_data = len(game_data) - 1

    data_departure = {'option_user': option_user, 'games_played': len_game_data}

    if len_game_data == 0:
        value_to_vet = get_value_to_bet()

        data_departure.setdefault('full_value_bet', value_to_vet)
        data_departure.setdefault('value_to_bet', value_to_vet)

        data_game = get_winner(data_departure)

    elif len_game_data > 0:

        data_departure.setdefault('full_value_bet', full_value_bet['current_value'])

        if full_value_bet['is_winner'] and full_value_bet['current_value'] != 0:
            data_departure.setdefault('value_to_bet', full_value_bet['current_value'])
            data_game = get_winner(data_departure)
        else:
            data_departure.setdefault('value_to_bet', get_value_to_bet())
            data_game = get_winner(data_departure)

    else:
        data_departure.setdefault('full_value_bet', full_value_bet['current_value'])
        data_departure.setdefault('value_to_bet', get_value_to_bet())

        data_game = get_winner(data_departure)

    game_data.append(data_game)
    return


def get_value_to_bet():
    print()
    value_to_bet = input('Ingresa el valor a apostar: ')

    if not value_to_bet.isnumeric() or int(value_to_bet) <= 0:
        print('Valor incorrecto, por favor...')
        return get_value_to_bet()
    return int(value_to_bet)


game_start()
