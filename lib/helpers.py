from models.genre import Genre
from models.band import Band


#//////////////////////////////////////////  Main Menu  ////////////////////////////////////////////

def list_genres():
    return Genre.get_all()

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
    name = input("Enter genre name: ")
    try:
        genre = Genre.create(name)
        print(f"Genre {genre.name} successfully created!")
    except Exception as exc:
        print("Error creating genre: ", exc)
    main_menu()

#### Genre list
def genres_menu_choices(): 
    genres = list_genres()   
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
    name_ = input("Enter the name of the genre you want to delete: ")
    if genre := Genre.find_by_name(name_):
        genre.delete()
        print(f"Genre {name_} deleted successfully.")
    else:
        print(f"Genre '{name_}' not found!")
    main_menu()

#### Genre helping methods
def selecting_genre():
    name_ = input("Enter genre name: ")
    if genre := Genre.find_by_name(name_):
        try:
            name = input("Enter the genre's new name: ")
            genre.name = name

            genre.update()
            print(f"Genre {name_} successfully updated to {genre.name}!")
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print(f"Genre {name_} not found!")
    main_menu()

#### Print Genre List
def print_genre_list():
    genres = list_genres()
    starting_lines_for_genre_methods()
    print("             GENRE LIST       \n")
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")

#*************** Genre Table Helper Methods ********************************

def print_line():
    print("\n-------------------------------------------------\n")

def starting_lines_for_genre_methods():
    print_line() 
    print("Welcome to the World's Top Music Store")
    print("      ROCK STARS OF THE WORLDS       \n\n")   

def ending_lines_for_genre_methods():
    print("\nPress 'b' to go back Main Menu.")
    print("Press 'e' to exit the program.")    
    print_line()

#///////////////////////////////////////////////////////////////////////////////////////////////

def band_menu(genre):
    print("Genre: " + genre)

def exit_program():
    print("Goodbye!")
    exit()