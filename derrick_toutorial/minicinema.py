movie = []       
def menu():
    user_input = input("Enter 'a' to add a movie, 'i' to see your movies, 'f' to find a movie, 'q' to quit: " )
    while user_input != 'q':
        if user_input == 'a':
            add_movies()
        elif user_input == 'i':
            show_movies()
        elif user_input == 'f':
            find_movives()
        elif user_input == 'q':
            print("stopping program..")
        else:
            print("Unkown command")
        user_input = input("Enter 'a' to add a movie, 'i' to see your movies, 'f' to find a movie, 'q' to quit: " )



def add_movies():
    Name = input("Enter The name of the Movie: ")
    Director = input("Enter The Director of the Movie: ")
    year = int(input("Enter The year of the Movie: ")) 
     
    movie.append({'Name': Name,
                 'Director': Director,
                 'Year' : year
    })

def show_movies():
    for x in movie:
        print(f"Name:{movie['Name']}")
        print(f"Director:{movie['Director']}")
        print(f"Year:{movie['year']}")
menu()
