# lib/cli.py

from helpers import (
    print_line,
    exit_program,
    create_genre,
    list_genres,
    find_genre_by_name,
    delete_genre 
)


def main():
    main_menu()

#**********************************  Genre Menu Methods ******************************************

genres = list_genres()
   
def main_menu():    
    def new_genre():
        create_genre()
        main_menu()

    functions = [("Create Genre", new_genre), ("Genre List", genres_menu_choices), ("Choose Genre", selecting_genre), ("Delete", delete_genre)]

    choice = ''
    
    print_line()
    print("Welcome to the World's Top Music Store\n")
    print("      ROCK STARS OF THE WORLDS       \n\n\n\n")
    print("Please select music genre or add new one:\n")
    
    #print Genre menu 
    for index in range(len(functions)):
        print(f"{index + 1}: {functions[index][0]}")

    print("\nPress 'e' to exit the program.")
    print_line()  

    #selecting Genre menu
    while choice != 'e':        
        choice = input("> ")  
        for index in range(len(functions)):
            if choice == str(index):
                functions[index - 1][1]()
                break
        if choice == "e":
            exit_program()
        else:
            print("Invalid choice")  

def genres_menu_choices():    
    print_genre_list()
    ending_lines_for_genre_methods()
    choice = input("> ")
    while choice != 'e' or choice != 'm':
        if choice.isdigit() and 0 < int(choice) <= len(genres):
            band_menu(genres[int(choice) - 1])
        elif choice == 'm':
            main_menu()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice")
        choice = input("> ")

def selecting_genre():
    print_genre_list()
    selected = find_genre_by_name()
    ending_lines_for_genre_methods()
    print(f"{selected.name}")

def print_genre_list():
    starting_lines_for_genre_methods()
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")

def starting_lines_for_genre_methods():
    print_line()
    print("Please select genre to see bands of that genre:\n")

def ending_lines_for_genre_methods():
    print("\nPress 'm' to go back Main Menu.")
    print("Press 'e' to exit the program.")
    print_line()

#**********************************************************************************************

def band_menu(genre):
    pass


if __name__ == "__main__":
    main()
