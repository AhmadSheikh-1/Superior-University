print()

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def calculate_average_budget(movies):
    total_budget = 0
    for movie in movies:
        total_budget += movie[1]
    return total_budget / len(movies) if movies else 0

def find_high_budget_movies(movies, average_budget):
    return [(title, budget, budget - average_budget) for title, budget in movies if budget > average_budget]

def add_movies(movies):
    number_of_movies = int(input("How many movies do you want to add? "))
    
    for i in range(number_of_movies):
        movie_title = input("Enter the movie title: ")
        movie_budget = int(input("Enter the movie budget: "))
        movies.append((movie_title, movie_budget))

def main():
    print("Welcome to the Movie Budget Analyzer"  )
    add_movies(movies)
    average_budget = calculate_average_budget(movies)
    print(f"\nThe average movie budget is: $ {average_budget:}\n" ) 
    
    high_budget_movies = find_high_budget_movies(movies, average_budget)
    
    if high_budget_movies:
        
        print("Movies with a budget higher than the average: ")
        for title, budget, difference in high_budget_movies:
            print(f"{title} had a budget of ${budget:,}, which is ${difference:,} above the average. "  )
        print(f"\nNumber of movies with a budget above average: {len(high_budget_movies)}")
    else:
        print("No movies have a budget higher than the average ")

main()

