# lib/cli.py

from helpers import (
    print_line,
    exit_program,
    create_genre,
    list_genres
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_genre()
        elif choice == "2":
            list_genres()
        else:
            print("Invalid choice")


def menu():
    print_line()
    print("Welcome to the World's Top Music Store\n")
    print("      ROCK STARS OF THE WORLDS       \n\n\n\n")
    print("Please select music genre or add new one:\n")
    print("0. Exit the program")
    print("1. Create Genre")
    print("2. List of genres")
    print_line()


if __name__ == "__main__":
    main()
