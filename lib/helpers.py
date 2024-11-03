from models.genre import Genre
from models.band import Band

def print_line():
    print("\n-------------------------------------------------\n")

def create_genre():
    name = input("Enter genre name: ")
    try:
        genre = Genre.create(name)
        print(f"Genre {genre.name} successfully created!")
    except Exception as exc:
        print("Error creating genre: ", exc)

def list_genres():
    return Genre.get_all()

def update_genre():
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


def delete_genre():
    name_ = input("Enter the name of the genre you want to delete: ")
    if genre := Genre.find_by_name(name_):
        genre.delete()
        print(f"Genre {name_} deleted successfully.")
    else:
        print(f"Genre '{name_}' not found!")

def exit_program():
    print("Goodbye!")
    exit()