def settings(temp):

    temp = input("czy chcesz zmienić znaki graczy: ")
    if 't' == input("czy chcesz zmienić znak gracza: ").lower()[0]:
        while True:
            temp1 = input("Wprowadź znak gracza 1: ")[0]
            temp2 = input("Wprowadź znak gracza 2: ")[0]
            if temp[1] != temp[2]:
                temp[1] = temp1
                temp[2] = temp2
                break
            else:
                print("Znaki nie mogą być takie same!")

    if 't' == input("czy chcesz zmienić punktacje: ").lower()[0]:
        while True:
            temp0 = input("Wprowadź ilość rund do wygrania: ")

            if temp0.isnumeric() and int(temp0) > 0:
                temp[0] = temp0
                break
            else:
                print("Musi być więcej niż 1 potyczka!")

    print(f"G1 - '{temp[1]}', G2 - '{temp[2]}', do ilu punktów {temp[0]}")
    return temp
