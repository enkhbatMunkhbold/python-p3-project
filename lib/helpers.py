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
    # genres = Genre.get_all()
    # for genre in genres:
    #     print(genre)
    return Genre.get_all()


def exit_program():
    print("Goodbye!")
    exit()
