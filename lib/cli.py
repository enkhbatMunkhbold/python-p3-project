# lib/cli.py

from helpers import (
    print_line,
    exit_program,
    create_genre,
    list_genres,
    update_genre,
    delete_genre 
)


def main():
    main_menu()

#**********************************  Main Menu  ******************************************

def main_menu():    
    
    functions = [("Create Genre", new_genre), ("Genre List", genres_menu_choices), ("Update Genre's name", selecting_genre), ("Delete", delete_chosen_genre)]
    choice = ''

    #print Main Menu     
    starting_lines_for_genre_methods()      
    print("             MAIN MENU       \n\n")
    for index in range(len(functions)):
        print(f"{index + 1}: {functions[index][0]}")    
    
    print("\nPress 'e' to exit the program.")    
    print_line()  

    #calling methods in Genre menu
    while True:        
        choice = input("> ")  
        for index in range(len(functions) + 1):
            if choice == str(index):
                functions[index - 1][1]()
                break
        if choice == "e":
            exit_program()
        elif 1 > int(choice) > len(functions):
            print("Invalid choice") 

#### Create new Genre
def new_genre():
        create_genre()
        main_menu()
        # print_genre_list()

#### Genre list
def genres_menu_choices():    
    print_genre_list()
    print("\nPlease select music genre to find out more!")
    ending_lines_for_genre_methods()
    choice = input("> ")
    while choice != 'e' or choice != 'm':
        if choice.isdigit() and 0 < int(choice) <= len(genres):
            band_menu(genres[int(choice) - 1])
        elif choice == 'b':
            main_menu()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice")
        choice = input("> ")

#### Genre delete
def delete_chosen_genre():
    delete_genre()
    main_menu()

#### Genre helping methods
def selecting_genre():
    update_genre()
    main_menu()
    # print(f"Chosen genre: {chosen_genre.name}")
    # print_genre_list()
    # choice = input("> ")    
    # for index in range(len(genres)):
    #     if choice == str(index + 1):
    #         print(f"Selected genre: {genres[index].name}")
    #         break
    # print("\nPlease select genre to see bands of that genre!")
    # ending_lines_for_genre_methods()

def print_genre_list():
    genres = list_genres()
    starting_lines_for_genre_methods()
    print("             GENRE LIST       \n")
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")

def starting_lines_for_genre_methods():
    print_line() 
    print("Welcome to the World's Top Music Store")
    print("      ROCK STARS OF THE WORLDS       \n\n")   

def ending_lines_for_genre_methods():
    print("\nPress 'b' to go back Main Menu.")
    print("Press 'e' to exit the program.")    
    print_line()

#**********************************************************************************************

def band_menu(genre):
    print("Genre: " + genre)


if __name__ == "__main__":
    main()
