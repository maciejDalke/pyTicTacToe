import game
import game_settings
import messages as m

char_tab = ['O', 'X']
first_player_start = True
this_game_number = 1
max_game_number = 3
score = [0, 0]
m.welcome_message()
m.menu()

while True:
    keyboard = input("Gotów - ").lower()[0]
    match keyboard:
        case 'y':
            while score[0] < max_game_number and score[1] < max_game_number:
                temp_point = game.start(char_tab,
                                        first_player_start,
                                        this_game_number,
                                        max_game_number)
                this_game_number += 1
                if temp_point == 1:
                    score[0] += 1
                elif temp_point == 2:
                    score[1] += 1
                print(score)

            print(f"wynik potyczki {score}")

            if score[0] == max_game_number:
                print("Wygrał gracz 1")
                break
            elif score[0] == max_game_number:
                print("Wygrał gracz 2")
                break

        case 'i':
            m.settings_information(max_game_number, char_tab)

        case 's':
            print("settings")
            temp = [max_game_number, char_tab[0], char_tab[1]]
            temp = game_settings.settings(temp)
            max_game_number = int(temp[0])
            char_tab[0] = temp[1]
            char_tab[1] = temp[2]

        case 'r':
            print("Ustawienia początkowe zostały załadowane")
            char_tab = ['O', 'X']
            first_player_start = True
            this_game_number = 1
            max_game_number = 3

        case 'q':
            break

print("Żegnam cieplutko")
