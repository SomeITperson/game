choices_list = {1 :{"Камень" : "Ножницы"},
                2 : {"Ножницы" : "Бумага"},
                3 : {"Бумага" : "Камень"}}
def choice():
    while True:
        user_1 = input("Имя первого игрока: ")
        user_2 = input("Имя второго игрока: ")
        if user_1 == user_2:
            print("---Выберите другие имена---")
            continue
        print("\n" * 10)
        for numbers, choices  in choices_list.items():
            for u1, u2 in choices.items():
                print(f"{numbers}. {u1}")
        user_1_c = input(f"{user_1}, выберите действие(камень, ножницы, бумага): ").title()
        print("\n" * 10)
        for numbers, choices in choices_list.items():
            for u1, u2 in choices.items():
                print(f"{numbers}. {u1}")
        user_2_c = input(f"{user_2}, выберите действие(камень, ножницы, бумага): ").title()
        break
    for user_choice_2, win_choice_2 in choices_list.items():
        for user_choice, win_choice in win_choice_2.items():
            if user_1_c == user_choice:
                if user_2_c == win_choice:
                    print(f"\n\t\t--->{user_1}, вы победили<---")
                elif user_1_c == user_2_c:
                    print(f"\n\t\t---Ничья---")
                else:
                    print(f"\n\t\t--->{user_2}, вы победили<---")

def main():
    choice()

if __name__ == "__main__":
    main()