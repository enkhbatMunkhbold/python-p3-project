# lib/cli.py

from helpers import (
    print_line,
    exit_program,
    create_genre,
    list_genres
)


def main():
    main_menu()
    
def main_menu():
    choice = ''
    main_menu_choices()
    while choice != 'e':        
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "1":
            create_genre()
            main_menu_choices()
        elif choice == "2":
            genres_menu_choices()
        else:
            print("Invalid choice")



def main_menu_choices():
    print_line()
    print("Welcome to the World's Top Music Store\n")
    print("      ROCK STARS OF THE WORLDS       \n\n\n\n")
    print("Please select music genre or add new one:\n")
    print("Exit the program, press 'e'")
    print("1. Create Genre")
    print("2. List of genres")
    print_line()

def genres_menu():
    pass

def genres_menu_choices():
    genres = list_genres()
    print_line()
    print("Please select genre to see bands of that genre:\n")
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")
    print("\nPress 'm' to go back Main Menu.")
    print("Press 'e' to exit the program.")
    print_line()
    choice = input("> ")
    while choice != 'e' or choice != 'm':
        if choice.isdigit() and 0 < int(choice) <= len(genres):
            band_menu(genres[int(choice) - 1])
        elif choice == 'm':
            main_menu()
        else:
            print("Invalid choice")
        choice = input("> ")

def band_menu(genre):
    pass


if __name__ == "__main__":
    main()
