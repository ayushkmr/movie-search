"""
This module is responsible for searching through indexed movie data.
"""

from collections import defaultdict
from typing import Dict, List
from src.index import Index


class Search:
    """
    A class used to represent a search engine that uses the index to perform searches. 

    Attributes
    ----------
    index : Dict[str, List[str]]
        An index containing words mapped to movie names where it appears.
    num_results : int
        The number of search results to display.

    Methods
    -------
    perform_search(query: str)
        Performs a search using the query, and prints out the search results.
    """
    def __init__(self, index: Index, num_results: int = 3):
        """
        Constructs all the necessary attributes for the Search object.

        Parameters
        ----------
            index : Index
                An index object that the Search object will use to perform searches.
            num_results : int
                The number of search results to display (default is 3).
        """
        self.index = index.index
        self.num_results = num_results

    def perform_search(self, query: str):
        """
        Performs a search using the query, and prints out the search results.

        Parameters
        ----------
        query : str
            The search query.
        """
        results = defaultdict(int)
        for word in query.lower().split():
            for movie_name in self.index[word]:
                results[movie_name] += 1
        results = sorted(results.items(), key=lambda x: x[1], reverse=True)[:self.num_results]
        for movie_name, _ in results:
            print(movie_name)
