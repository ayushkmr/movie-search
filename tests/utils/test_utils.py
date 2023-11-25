import unittest
import json
import sys
import os

# Add 'src' to your Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'movie-search')))

# Now you can import your custom modules
from src.models.movie import Movie
from src.utils.utils import movie_to_json, json_to_movie


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.sample_json = """
        {
            "actor": [
                {
                    "name": "James Stewart",
                    "@type": "Person",
                    "url": "/name/nm0000071/"
                },
                {
                    "name": "Kim Novak",
                    "@type": "Person",
                    "url": "/name/nm0001571/"
                },
                {
                    "name": "Barbara Bel Geddes",
                    "@type": "Person",
                    "url": "/name/nm0000895/"
                }
            ],
            "aggregateRating": {
                "bestRating": "10",
                "ratingCount": 402523,
                "ratingValue": 8.3,
                "@type": "AggregateRating",
                "worstRating": "1"
            },
            "contentRating": "PG",
            "@context": "https://schema.org",
            "creator": [
                {
                    "@type": "Organization",
                    "url": "/company/co0137799/"
                },
                {
                    "name": "Alec Coppel",
                    "@type": "Person",
                    "url": "/name/nm0178785/"
                },
                {
                    "name": "Samuel A. Taylor",
                    "@type": "Person",
                    "url": "/name/nm0853138/"
                },
                {
                    "name": "Pierre Boileau",
                    "@type": "Person",
                    "url": "/name/nm0092267/"
                }
            ],
            "datePublished": "1958-05-22",
            "description": "A former San Francisco police detective juggles wrestling with his personal demons and becoming obsessed with the hauntingly beautiful woman he has been hired to trail, who may be deeply disturbed.",
            "director": [
                {
                    "@type": "Person",
                    "url": "/name/nm0000033/",
                    "name": "Alfred Hitchcock"
                }
            ],
            "duration": "PT2H8M",
            "genre": [
                "Mystery",
                "Romance",
                "Thriller"
            ],
            "image": "https://m.media-amazon.com/images/M/MV5BYTE4ODEwZDUtNDFjOC00NjAxLWEzYTQtYTI1NGVmZmFlNjdiL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg",
            "keywords": "romantic obsession,san francisco bay,vertigo,1950s,acrophobia",
            "name": "Vertigo",
            "trailer": {
                "description": "Theatrical Trailer from Universal Studios Home Entertainment",
                "embedUrl": "https://www.imdb.com/video/imdb/vi216072473",
                "name": "Vertigo",
                "thumbnail": {
                    "contentUrl": "https://m.media-amazon.com/images/M/MV5BMDZkMDVhYTMtNzZiZS00YTYwLTk5ZmEtNmJmNGVjZDg2ZWM5XkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg",
                    "@type": "ImageObject"
                },
                "thumbnailUrl": "https://m.media-amazon.com/images/M/MV5BMDZkMDVhYTMtNzZiZS00YTYwLTk5ZmEtNmJmNGVjZDg2ZWM5XkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg",
                "@type": "VideoObject",
                "uploadDate": "2008-04-11T17:40:30Z"
            },
            "@type": "Movie",
            "url": "/title/tt0052357/"
        }
        """

    def test_movie_to_json(self):
        movie = json_to_movie(self.sample_json)
        json_string = movie_to_json(movie)
        expected_keys = {'name', 'actor', 'director', 'creator', 'genre', 
                        'keywords', 'aggregateRating', 'contentRating', 'description', 
                        'duration', 'image', 'url', 'datePublished', 'trailer', '@type'}
        print(json.dumps(movie.to_dict()))
        
        self.assertEqual(set(json.loads(json_string).keys()), expected_keys)

    def test_json_to_movie(self):
        movie = json_to_movie(self.sample_json)
        # print(movie)
        self.assertIsInstance(movie, Movie)
        self.assertEqual(movie.name, "Vertigo")

if __name__ == "__main__":
    unittest.main()