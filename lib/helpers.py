import json
from models.genre import Genre
from models.band import Band


#//////////////////////////////////////////  MAIN MENU  ////////////////////////////////////////////

def list_genres():
    return Genre.get_all()
def list_of_bands():
    return Band.get_all()

def genre_menu():    
    
    functions = [("C", "Create Genre", create_genre), ("U", "Update Genre's name", update_genre), ("D", "Delete", delete_genre), ("E", "Exit", exit_program)]
    selections = ["C", "U", "D", "E"]
    
    #print Main Menu   
    if (list_genres()):
        print_genre_list()
    else:
        print("There is no Genre created yet!")
    print("\n\n") 
    
    for index in range(len(functions)):
        print(f"{functions[index][0]}: {functions[index][1]}")    
    print_line() 
    choice = input("> ").upper() 
    if choice in selections:
        select_managing_methods(choice, functions, selections)
    else:
        # print('Selected Genre')
        select_genre_from_list(choice)

#*****************  calling methods in Main menu  ****************
def select_managing_methods(select, data_list1, data_list2 ):
    while True:  
        for index in range(len(data_list1) + 1):
            if select == data_list1[index - 1][0]:
                data_list1[index - 1][2]()
                break
        if select not in data_list2:
            print("Invalid choice") 

#*****************   Main menu create genre   *******************
def create_genre():
    name = input("Enter genre name: ").title()
    if Genre.find_by_name(name):
        return None
    else:
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

def print_bands_list(genre):
    bands = Band.get_by_genre(genre.id)
    for index, band in enumerate(bands):
        print(f"{index + 1}: {band.name}")

#//////////////////////////////////   CHOSEN GENRE MENU  //////////////////////////////////////////////////

def chosen_genre_menu(genre):
    options = [("A", "Add Band", add_band), ("U", "Update Band name", update_band), ("D", "Delete", delete_band)]
    keys = ["A", "U", "D"]
    starting_lines_for_submenu()
        
    print(f"            GENRE: {genre.name.upper()}     \n\n")

    if(list_of_bands()):
        print_bands_list(genre)
        print("\n\n")
    else:
        print(f"There is no {genre.name.title()} band in this list, yet!\n\n")

    for index in range(len(options)):
        print(f"{options[index][0]}: {options[index][1]}")
    ending_lines_for_genre_methods()    

    choice = ''
    while True:
        choice = input("> ").upper()
        if choice in keys:
            for index in range(len(options)):
                if choice == options[index][0]:
                    if choice == "A":
                        options[index][2](genre.id)
                    else:
                        options[index][2]()
        elif choice.isdigit():
            bands = Band.get_by_genre(genre.id)
            for index, band in enumerate(bands):
                if index + 1 == int(choice):
                    band_menu(band)
        elif choice == 'B':
            genre_menu()
        elif choice == 'E':
            exit_program()
        else:
            print("Invalid choice")    
   
def exit_program():
    print("Goodbye!")
    exit()

#////////////////////////////////////////    BAND MENU   /////////////////////////////////////////////

def band_menu(group):
    
    starting_lines_for_submenu()
    print(f"            BAND: {group.name.upper()}\n\n") 
    print("Band Members:\n")
    member_names = json.loads(group.members)
    for index, member in enumerate(member_names):
        print(f"{index + 1}: {member}")

    ending_lines_for_genre_methods()    

def add_band(genre_id):

    name = input("Enter band name: ").title()    
    if Band.find_by_name(name):
        print("The band is already exists in the list!")
        genre_menu()
    else:
        number_of_members = input("Number of member in the band: ")
        members = []
        for index in range(int(number_of_members)):
            member = input(f"Enter name of member {index + 1}: ").title()
            members.append(member)  

        try:
            band = Band.create(name, genre_id, json.dumps(members))
            print(f"Band {band.name} has successfully created!")
            ending_lines_for_genre_methods()
        except Exception as exc:
            print("Error creating band: ", exc)
            ending_lines_for_genre_methods()

        band_menu(band)

def update_band():
    print("Updating Band...")

def delete_band():
    name_ = input("Enter the name of the band you want to delete: ").title()
    if band := Band.find_by_name(name_):
        band.delete()
        print(f"Band {name_} deleted successfully.")
    else:
        print(f"Band '{name_}' not found!")
    genre_menu()