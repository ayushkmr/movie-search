"""
main.py
This file serves as the driver script to load movies data, build index, and run the search engine.
"""

from src.utils.utils import load_movies_from_json_file
from src.index import Index
from src.search import Search
from src.models.movie import Movie
from typing import List


def main():
    """ The main function of the search program. """
    
    # Load movies from JSON file
    movies: List[Movie] = load_movies_from_json_file("movies.json")
    
    # Ask user for number of results to display
    num_results: str = input("Enter the number of top relevant movie names to display (default is 3): ")
    num_results: int = int(num_results) if num_results.isdigit() else 3

    # Create index
    index: Index = Index(movies)
    
    # Create search engine using the index
    search: Search = Search(index, num_results)
    
    # Keep the search running until the user wants to exit
    while True:
        print("\n[INFO] Type 'exit' to quit the program.")
        query: str = input("\nEnter your search query: ")
        
        # If the query is 'exit', break the loop
        if query.lower() == "exit":
            print("[INFO] Exiting the program.")
            break
        
        # Perform search
        search.perform_search(query)


if __name__ == "__main__":
    main()
