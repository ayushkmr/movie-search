import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
from datetime import datetime

# Update the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'movie-search')))

from src.utils.utils import load_movies_from_json_file
from src.utils.search_utils import *


class TestSearchUtils(unittest.TestCase):

    def setUp(self):
        """
        Setting up for the test
        """
        self.movies = load_movies_from_json_file("./tests/test_movies.json")
        self.movies_by_name = {movie.name.lower(): movie for movie in self.movies}

    def test_print_results(self):
        """
        Test print_results function
        """
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            print_results(self.movies, 1)
            assert "Top 1 result(s):\n\tTop Gun: Maverick" in fake_out.getvalue()

    def test_print_no_result_message(self):
        """
        Test print_no_result_message function
        """
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            print_no_result_message("No movies found with your criteria.", self.movies)
            assert "Showing top-rated movies instead:" in fake_out.getvalue()

    def test_get_movies_by_year(self):
        """
        Test get_movies_by_year function
        """
        year_index = {2010: [movie for movie in self.movies if movie.year == 2010]}
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            get_movies_by_year(year_index, 2010, 1)
            self.assertIn('Toy Story 3', mock_stdout.getvalue())

    def test_sort_by_rating(self):
        """
        Test sort_by_rating function
        """
        top_movies = sort_by_rating(self.movies, 1)
        self.assertEqual(top_movies[0].name, "Top Gun: Maverick")

    def test_try_parse_date(self):
        """
        Test try_parse_date function
        """
        parsed_date = try_parse_date("2010-06-18")
        self.assertEqual(parsed_date, datetime(2010, 6, 18))

        parsed_date = try_parse_date("invalid date")
        self.assertEqual(parsed_date, None)

    def test_perform_full_query_search(self):
        """
        Test perform_full_query_search function
        """
        index = {movie.name.lower(): [movie] for movie in self.movies}
        query = "Toy Story 3"
        movies = perform_full_query_search(index, query)
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].name, query)

    def test_perform_chunked_query_search(self):
        """
        Test perform_chunked_query_search function
        """
        index = {word.lower(): [movie] for movie in self.movies for word in movie.name.split()}
        query = "Toy"
        movies = perform_chunked_query_search(index, query)
        self.assertEqual(len(movies), 2)
        self.assertListEqual([movie.name for movie in movies], ["Toy Story", "Toy Story 3"])

if __name__ == "__main__":
    unittest.main()