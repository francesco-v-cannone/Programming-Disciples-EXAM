import json

class MovieNotFoundError(Exception):
    pass

class MovieLibrary:
    def __init__(self, json_file, movies):
        self.json_file = json_file
        self.movies = movies
        try:
            with open(self.json_file, 'r') as file:
                self.movies = json.load(file)
#17. Modifica il metodo costruttore affinché,
#se nel percorso json_file non viene trovato alcun file,
#venga sollevata l’eccezione FileNotFoundError
#col messaggio personalizzato “File not found: ” seguito dal percorso json_file.        
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")

    def __update_json_file(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.movies, file, indent=4)
#1. Crea un metodo chiamato get_movies che restituisce l’intera collezione di film.
    def get_movies(self):
        return self.movies
#2. Crea un metodo chiamato add_movie che ha i parametri title e director di tipo stringa,
#year di tipo intero e genres di tipo lista (di stringhe).
#Il metodo aggiunge il film alla collezione e aggiorna il file json.
    def add_movie(self, title, director, year, genres):
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genre": genres
        }
        self.movies.append(new_movie)
        self.__update_json_file()
#3. Crea un metodo chiamato remove_movie che ha il parametro title.
#Il metodo rimuove dalla collezione il film
#che ha titolo corrispondente (NON case sensitive) a title.
#Il metodo aggiorna il file json e restituisce il film rimosso.
    def remove_movie(self, title):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
#18. Modifica i metodi remove_movie e update_movie affinché,
#se non viene trovato alcun film avente come titolo title,
#venga sollevata l’eccezione personalizzata MovieNotFoundError,
#avente il messaggio “Movie was not found”.
#Tale eccezione va definita all’interno della classe MovieLibrary.        
        raise MovieNotFoundError("Movie was not found")
#4. Crea un metodo chiamato update_movie che ha il parametro title
#e i parametri opzionali director, year e genres.
#Il metodo ricerca nella collezione il film
#che ha titolo corrispondente (NON case sensitive) a title.
#Quindi modifica il film,
#applicando il valore di ciascun parametro opzionale non nullo.
#Il metodo aggiorna il file json e restituisce il film coi valori aggiornati.
    def update_movie(self, title, director=None, year=None, genres=None):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director is not None:
                    movie["director"] = director
                if year is not None:
                    movie["year"] = year
                if genres is not None:
                    movie["genre"] = genres
                self.__update_json_file()
                return movie
#18bis.        
        raise MovieNotFoundError("Movie was not found")
#5. Crea un metodo chiamato get_movie_titles
#che restituisce una lista contenente tutti i titoli dei film nella collezione.
    def get_movie_titles(self):
        return [movie["title"] for movie in self.movies]
#6. Crea un metodo chiamato count_movies
#che restituisce il numero totale dei film nella collezione.
    def count_movies(self):
        return len(self.movies)
#7. Crea un metodo chiamato get_movie_by_title che ha il parametro title.
#Il metodo restituisce il film che ha titolo corrispondente (NON case sensitive) a title.
    def get_movie_by_title(self, title):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie
        return None
#8. Crea un metodo chiamato get_movies_by_title_substring
#che ha il parametro substring.
#Il metodo restituisce una lista di tutti i film che contengono, nel titolo,
#una sottostringa corrispondente (case sensitive) a substring.
    def get_movies_by_title_substring(self, substring):
        return [movie for movie in self.movies if substring in movie["title"]]
#9. Crea un metodo chiamato get_movies_by_year che ha il parametro year.
#Il metodo restituisce una lista di tutti i film con anno corrispondente a year.
    def get_movies_by_year(self, year):
        return [movie for movie in self.movies if movie["year"] == year]
#10. Crea un metodo chiamato count_movies_by_director che ha il parametro director.
#Il metodo restituisce il numero di film diretti dal regista corrispondente (NON case sensitive) a director. 
    def count_movies_by_director(self, director):
        return sum(1 for movie in self.movies if movie["director"].lower() == director.lower())
#11. Crea un metodo chiamato get_movies_by_genre che ha il parametro genre.
#Il metodo restituisce una lista di tutti i film che appartengono al genere corrispondente (NON case sensitive) a genre.
    def get_movies_by_genre(self, genre):
        return [movie for movie in self.movies if genre.lower() in (g.lower() for g in movie["genre"])]
#12. Crea un metodo chiamato get_oldest_movie_title che restituisce il titolo del film più vecchio.
#Se ci sono più film con la stessa data di uscita, restituire il primo trovato.
    def get_oldest_movie_title(self):
        oldest_movie = min(self.movies, key=lambda movie: movie["year"])
        return oldest_movie["title"]
#13. Crea un metodo chiamato get_average_release_year che restituisce
#un float rappresentante la media aritmetica degli anni di pubblicazione
#dei film della collezione. Il float viene di per se restituito dalla divisione, non so se serve 
#aggiungere il float() davanti alla divisione, nel dubbio l'ho messo.
    def get_average_release_year(self):
        return float(sum(movie["year"] for movie in self.movies) / len(self.movies))
#14. Crea un metodo chiamato get_longest_title che restituisce il titolo
#più lungo della collezione di film.
    def get_longest_title(self):
        return max(self.movies, key=lambda movie: len(movie["title"]))["title"]
#15. Crea un metodo chiamato get_titles_between_years che ha due parametri:
#start_year e end_year.
#Il metodo restituisce una lista contenente i titoli dei film pubblicati
#dall’anno start_year fino all’anno end_year (estremi compresi).
    def get_titles_between_years(self, start_year, end_year):
        return [
            movie["title"]
            for movie in self.movies
            if start_year <= movie["year"] <= end_year
        ]
#16. Crea un metodo chiamato get_most_common_year
#che restituisce l’anno che si ripete più spesso fra i film della collezione.
#Non considerare il caso in cui vi siano pari merito.
def get_most_common_year(self):
    """Restituisce l'anno più comune tra i film nella collezione."""
    years = [movie["year"] for movie in self.movies]
    if not years:
        return None
    return max(set(years), key=years.count)
