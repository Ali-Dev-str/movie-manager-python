class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def __repr__(self):
        return f" {self.title} ({self.year}) - Directed by: {self.director} [Rating: {self.rating}/10]"


class MovieManager: 
    def __init__(self):
        self.movies = []


    def add_movie(self, movie):
        self.movies.append(movie)
        print(f" Added successfully: {movie.title}")


    def remove_movie(self, movie_title):
        for mov in self.movies:
            if mov.title.lower() == movie_title.lower():
                self.movies.remove(mov)
                print(f" Removed successfully: {movie_title}")
                return True
        print(" Movie not found!")
        return False

    def search_movie(self, movie_title):
        for mov in self.movies:
            if mov.title.lower() == movie_title.lower():
                return mov
        return None

    def show_movies(self):
        return self.movies



if __name__ == "__main__":
    manager = MovieManager()
    
    movie1 = Movie("Inception", "Christopher Nolan", 2010, 8.8)
    movie2 = Movie("The Dark Knight", "Christopher Nolan", 2008, 9.0)
    
    manager.add_movie(movie1)
    manager.add_movie(movie2)
    
    print("\n--- All Movies ---")
    for m in manager.show_movies():
        print(m)
        
    print("\n--- Searching for Inception ---")
    result = manager.search_movie("Inception")
    print(result if result else "Not Found")
    
    print("\n--- Removing a Movie ---")
    manager.remove_movie("Inception")