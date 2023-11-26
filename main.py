"""
This file serves as the driver script to load movies data, build index, and run the search engine.
"""

from src.utils.utils import load_movies_from_json_file
from src.index import Index
from src.search import Search
from src.models.movie import Movie
from typing import List
import os
import certifi
import nltk

os.environ['SSL_CERT_FILE'] = certifi.where()
nltk.download('stopwords')

def main():
    """ The main function of the search program. """
    
    # Load movies from JSON file
    movies: List[Movie] = load_movies_from_json_file("movies.json")

    # Default configuration
    num_results: int = 3
    no_result_message = 'No results found'

    # Create index
    index: Index = Index(movies)

    # Create search engine using the index
    search = Search(index, num_results)
    
    print("\n[INFO] Type 'exit' to quit the program.")
    print("[INFO] Type '--configure' to open the configuration menu.")

    # Keep the search running until the user wants to exit
    while True:
        query: str = input("\nEnter your search query or year: ")
        
        # If the query is 'exit', break the loop
        if query.lower() == "exit":
            print("\n[INFO] Exiting the program.")
            break

        # If the query is '--configure', open the configuration menu
        elif query.lower() == '--configure':
            print("\n***Configuration Menu***")
            num_results_input = input("\nEnter the number of top relevant movie names to display (default is 3): ")
            num_results = int(num_results_input) if num_results_input.isdigit() else num_results
            
            no_result_message_input = input("\nEnter the message to display when no results are found (default is 'No results found'): ")
            no_result_message = no_result_message_input if no_result_message_input != '' else no_result_message

            # Update search with the new configuration
            search = Search(index, num_results, no_result_message)
            print("\nConfiguration updated!")
            
        # If the input is a year (only contains digits) and the year exists in the year index
        elif query.isdigit() and int(query) in index.year_index.keys():
            year = int(query)
            search.get_movies_by_year(year)

        # Perform search on general query
        else:
            search.perform_search(query)
        
        print("________________________________________________________________")
        


if __name__ == "__main__":
    main()