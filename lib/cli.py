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
    print("\nPress 'm' to go back Main Menu!")
    print("To exit the program type 'e'")
    print_line()


if __name__ == "__main__":
    main()
