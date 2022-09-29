import temp


def welcome_message():
    print("""
            Kółko i krzyżyk
    
        Grę utworzył: Maciej Dalke    """)


def menu():
    print("""  Menu:
    'Y' - żeby zagrać
    'I' - pokaż ustawienia gry
    'S' - wejście w ustawienia
    'R' - aby zrestartować grę
    'Q' - wyjście z gry
    """)


def settings_information(max_game_number, char_tab):
    print(f"""Gra najlepszy z {max_game_number}
    Gracz pierwszy - '{char_tab[0]}'
       Gracz drugi - '{char_tab[1]}'
""")


def game_board():
    game_board_with_shots(temp.numbers)


def game_board_with_shots(shots):
    print(f"""
     {shots[0]} | {shots[1]} | {shots[2]} 
    -----------
     {shots[3]} | {shots[4]} | {shots[5]}
    -----------
     {shots[6]} | {shots[7]} | {shots[8]}
     """)
