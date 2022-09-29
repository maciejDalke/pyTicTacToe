import messages as m

board_with_shots = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def is_win(p_char):
    if ((board_with_shots[0] == p_char and board_with_shots[1] == p_char and board_with_shots[2] == p_char) or
            (board_with_shots[3] == p_char and board_with_shots[4] == p_char and board_with_shots[5] == p_char) or
            (board_with_shots[6] == p_char and board_with_shots[7] == p_char and board_with_shots[8] == p_char) or
            (board_with_shots[0] == p_char and board_with_shots[3] == p_char and board_with_shots[6] == p_char) or
            (board_with_shots[1] == p_char and board_with_shots[4] == p_char and board_with_shots[7] == p_char) or
            (board_with_shots[2] == p_char and board_with_shots[5] == p_char and board_with_shots[8] == p_char) or
            (board_with_shots[0] == p_char and board_with_shots[4] == p_char and board_with_shots[8] == p_char) or
            (board_with_shots[2] == p_char and board_with_shots[4] == p_char and board_with_shots[6] == p_char)):
        return True
    pass


def reset_board():
    for i in range(0, 8):
        board_with_shots[i] = ' '
    print("reset")
    pass


def start(char_tab, player_play, round_number, max_game_number):
    print(f"    Game {round_number} of {max_game_number} begun:")
    m.game_board()
    print(f"Tę rozgrywkę rozpoczyna: {char_tab[int(player_play)]}")
    round_number = 1
    quit = True

    while True:
        # game
        while round_number < 10:
            # round
            shot = input(f"'{char_tab[int(player_play)]}' Pole: ")
            if shot is '':
                print("musisz coś wstawić! ")
            elif shot.isnumeric():
                shot = int(shot)
                if shot > 9 or shot < 1:
                    print("Nieoprawny numer pola")
                elif board_with_shots[shot - 1] == ' ':
                    board_with_shots[shot - 1] = char_tab[int(player_play)]
                    round_number = round_number + 1

                    print(m.game_board_with_shots(board_with_shots))
                    break
                else:
                    print("To pole jest niedostępne!")
            elif shot[0].lower() == 'q':
                print("quit")
                return -1
            else:
                print("Nie rozpoznany symbol!")

        # print(f" doooo {char_tab[int(player_play)].index() }")
        if round_number > 4 and is_win(char_tab[int(player_play)]):
            print(m.game_board_with_shots(board_with_shots))
            print(f"Gracz '{char_tab[int(player_play)]}' wygrał")
            reset_board()

            print(int(player_play) + 1)
            return int(player_play) + 1

        if round_number > 9:
            print("Remis!")
            return 0

        player_play = not player_play
