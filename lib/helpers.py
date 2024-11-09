from models.genre import Genre
from models.band import Band


#//////////////////////////////////////////  MAIN MENU  ////////////////////////////////////////////

def list_genres():
    return Genre.get_all()

def genre_menu():    
    
    functions = [("C", "Create Genre", create_genre), ("U", "Update Genre's name", update_genre), ("D", "Delete", delete_genre), ("E", "Exit", exit_program)]
    selections = ["C", "U", "D", "E"]
    
    #print Main Menu     
    starting_lines_for_submenu()  
    if (list_genres()):
        print_genre_list()
    else:
        print("There is no Genre created yet!")

    print("\n\n")    
    # print("             MAIN MENU       \n\n")
    
    for index in range(len(functions)):
        print(f"{functions[index][0]}: {functions[index][1]}")    
    print_line() 
    choice = input("> ").upper() 
    if choice in selections:
        select_managing_methods(choice, functions, selections)
    else:
        select_genre_from_list(choice)

#*****************  calling methods in Main menu  ****************
def select_managing_methods(select, data_list1, data_list2 ):
    # select = select.upper()
    while True:        
        # select = input("> ")  
        for index in range(len(data_list1) + 1):
            if select == data_list1[index - 1][0]:
                data_list1[index - 1][2]()
                break
        if select not in data_list2:
            print("Invalid choice") 

#*****************   Main menu create genre   *******************
def create_genre():
    name = input("Enter genre name: ").title()
    try:
        genre = Genre.create(name)
        print(f"Genre {genre.name} successfully created!")
    except Exception as exc:
        print("Error creating genre: ", exc)
    genre_menu()

#******************    Main Menu Genre list    *********************
def select_genre_from_list(select): 
    genres = list_genres()  
    for index, genre in enumerate(genres):
        if index + 1 == int(select):
            chosen_genre_menu(genre)
            break
    # chosen_genre_menu(select)
    # print_genre_list()
    # print("\nPlease select music genre to find out more!")
    # ending_lines_for_genre_methods()
    # choice = input("> ")
    # while int(select) < len(genres) :
    #     if 0 < int(select) <= len(genres):
    #         chosen_genre_menu(genres[int(select) - 1])
    #     # elif choice == 'b':
    #     #     genre_menu()
    #     # elif choice == 'e':
    #     #     exit_program()
    #     else:
    #         print("Invalid choice")
    #     # choice = input("> ")

#***************    Main menu delete    ******************
def delete_genre():
    name_ = input("Enter the name of the genre you want to delete: ").title()
    if genre := Genre.find_by_name(name_):
        genre.delete()
        print(f"Genre {name_} deleted successfully.")
    else:
        print(f"Genre '{name_}' not found!")
    genre_menu()

#***************    Main menu update methods   *******************
def update_genre():
    name_ = input("Enter genre name: ").title()
    if genre := Genre.find_by_name(name_):
        try:
            name = input("Enter the genre's new name: ").title()
            genre.name = name

            genre.update()
            print(f"Genre {name_} successfully updated to {genre.name}!")
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print(f"Genre {name_} not found!")
    genre_menu()

#************** Print Main Menu Genre List  ********************
def print_genre_list():
    genres = list_genres()
    starting_lines_for_submenu()
    print("             GENRE LIST       \n")
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")

#*************** Main Menu Helper Methods ********************************

def print_line():
    print("\n-------------------------------------------------\n")

def starting_lines_for_submenu():
    print_line() 
    print("Welcome to the World's Top Music Store")
    print("      ROCK STARS OF THE WORLDS       \n\n")   

def ending_lines_for_genre_methods():
    print("\nPress 'b' to go back Main Menu.")
    print("Press 'e' to exit the program.")    
    print_line()

#//////////////////////////////////   CHOSEN GENRE MENU  //////////////////////////////////////////////////

def chosen_genre_menu(genre):
    options = [("Insert Band", create_band), ("Band List", bands_list), ("Update Band name", update_band), ("Delete", delete_band)]
    starting_lines_for_submenu()
    # choice = input("> ")    
    print(f"            GENRE: {genre.name.upper()}     \n\n")
    for index in range(len(options)):
        print(f"{index + 1}: {options[index][0]}")
    # bands = Band.get_by_genre(genre.id)
    # while choice != 'e' or choice != 'm' or choice != 'l':
    #     if choice.isdigit() and 0 < int(choice) <= len(bands):
    #         band_menu(bands[int(choice) - 1])
    #     elif choice == 'b':
    #         genre_menu()
    #     elif choice == 'e':
    #         exit_program()
    #     else:
    #         print("Invalid choice")
    
        
    ending_lines_for_genre_methods()

def exit_program():
    print("Goodbye!")
    exit()

#////////////////////////////////////////    BAND MENU   /////////////////////////////////////////////

def band_menu():
    
    starting_lines_for_submenu()
    # print(f"            BAND: {band.name.upper()}")

    

    ending_lines_for_genre_methods()    

def create_band():
    print("Creating Band...")

def bands_list():
    print("List bands...")

def update_band():
    print("Updating Band...")

def delete_band():
    print("Deleting band...")