from models.genre import Genre
from models.band import Band

def print_line():
    print("\n-------------------------------------------------\n")

def create_genre():
    name = input("Enter genre name: ")
    try:
        genre = Genre.create(name)
        print(f"Success: {genre}")
    except Exception as exc:
        print("Error creating genre: ", exc)

def list_genres():
    return Genre.get_all()

def find_genre_by_name():
    name = input("Enter genre name: ")
    return Genre.find_by_name(name)

def delete_genre():
    name_ = input("Enter the name of the genre you want to delete: ")
    if genre := Genre.find_by_name(name_):
        genre.delete()
        print(f"Genre {name_} deleted successfully.")
    else:
        print(f"Genre '{name_}' not found.")

def exit_program():
    print("Goodbye!")
    exit()