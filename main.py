"""
This file serves as the driver script to load movies data, build index, and run the search engine.
"""

from src.utils.utils import load_movies_from_json_file
from src.index import Index
from src.search import Search
from src.models.movie import Movie
from typing import List, Set
import os
import certifi
import nltk
import logging

os.environ['SSL_CERT_FILE'] = certifi.where()
nltk.download('stopwords')

# Set up logger
logger = logging.getLogger('movie_search')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.CRITICAL)

def build_databases(movies: List[Movie]) -> dict:
    """
    Build databases for each category to be used in search engine.

    Attributes
    ----------
    movies : List[Movie]
        a list of Movie objects
    """
    years = set()
    actors = set()
    directors = set()
    creators = set()
    genres = set()
    movie_names = set(name for movie in movies for name in movie.name.split() + [movie.name])

    for movie in movies:
        years.add(movie.year)
        for actor in movie.actors:
            actors.add(actor.name)  # Add full name
            actors.update(actor.name.split())  # Add individual words
        for director in movie.directors:
            directors.add(director.name)
            directors.update(director.name.split())
        for creator in movie.creators:
            creators.add(creator.name)
            creators.update(creator.name.split())
        for genre in movie.genres:
            genres.add(genre.name)

    return {'years': years, 'actors': actors, 'directors': directors, 'creators': creators, 'genres': genres, 'movie_names': movie_names}

def main():
    """
    The main driver function of the search program.
    """
    # Load movies from the JSON file
    movies: List[Movie] = load_movies_from_json_file("movies.json")

    # Build databases
    databases = build_databases(movies)

    # Default configuration
    num_results: int = 10
    fuzz_ratio = 70

    # Create index
    index: Index = Index(movies)

    # Create search engine using the index
    search = Search(movies, index)
    
    print("\n[INFO] Type 'exit' to quit the program.")
    print("[INFO] Type '--configure' to open the configuration menu.")

    # Keep the search running until the user wants to exit
    while True:
        query: str = input("\nEnter your search query: ").strip()

        # If the query is 'exit', break the loop
        if query.lower() == "exit":
            logger.info("Exiting the program.")
            break

        # If the query is '--configure', open the configuration menu
        elif query.lower() == '--configure':
            logger.info("Entering configuration mode.")
            print("\n***Configuration Menu***")
            num_results_input = input("\nEnter the number of top relevant movie names to display (default is 10): ")
            num_results = int(num_results_input) if num_results_input.isdigit() else num_results
            print(f"\nTop number of results to display set to {num_results}")

            fuzz_ratio_input = input("\nEnter the fuzz ratio for fuzzy search (default is 70): ")
            fuzz_ratio = int(fuzz_ratio_input) if fuzz_ratio_input.isdigit() else fuzz_ratio
            print(f"\nFuzz ratio set to {fuzz_ratio}")

            debug_mode_input = input("\nTurn debug mode on? Enter 'y' for yes, 'n' for no: ")
            if debug_mode_input.lower() == 'y':
                search.logger.setLevel(logging.DEBUG)
                print("\nLogger set to debug mode.")
            else:
                search.logger.setLevel(logging.INFO)
                print("\nLogger set to info mode.")

        # Check all conditions individually instead of using elif to display all relevant details
        if query in databases['movie_names']:
            logger.info(f"Performing search by movie name for movie: {query}.")
            search.search_by_movie_name(query, num_results)

        if query.isnumeric() and int(query) in databases['years']:
            logger.info(f"Performing search by year for year: {query}.")
            search.search_by_year(int(query), num_results)

        if query in databases['actors']:
            logger.info(f"Performing search by actor for actor: {query}.")
            search.search_by_actor(query, num_results)

        if query in databases['directors']:
            logger.info(f"Performing search by director for director: {query}.")
            search.search_by_director(query, num_results)

        if query in databases['creators']:
            logger.info(f"Performing search by creator for creator: {query}.")
            search.search_by_creator(query, num_results)

        if query in databases['genres']:
            logger.info(f"Performing search by genre for genre: {query}.")
            search.search_by_genre(query, num_results)
        
        # Perform general search if no prior conditions matched
        if not any([query in databases[key] for key in databases.keys()]):
            logger.info(f"Performing general search for query: {query}.")
            search.general_search(query, fuzz_ratio, num_results)

        print("____________________________________________________________")

if __name__ == "__main__":
    main()