# lib/cli.py

from helpers import (
    print_line,
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print_line()
    print("Welcome to the World's Top Music Store\n")
    print("      ROCK STARS OF THE WORLDS       \n\n\n\n")
    print("Please select music genre or add new one:\n")
    print("0. Exit the program")
    print("1. Some useful function")
    print_line()


if __name__ == "__main__":
    main()
