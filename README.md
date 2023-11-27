# Movie Search Engine

A command-line based movie search engine that allows users to search for movie names based on one or several words related to the movie. The search engine also has the ability to display a list of the top-rated movies when no search results are found.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Configuration](#configuration)
5. [Assumptions](#assumptions)
6. [Possible Extensions](#possible-extensions)
7. [Contribute](#contribute)

## Installation

Follow the instructions below to run the search engine on your own machine:

1. Clone the repository:
```
git clone https://github.com/ayushkmr/movie-search.git
```

2. Change directory:
```
cd movie-search
```

3. Install required Python modules:
```
pip install -r requirements.txt
```

## Usage

To run the search engine, simply execute the `main.py` script:
```
python main.py
```

You will be prompted to enter a search query. You can enter a single keyword, multiple keywords to search for movies, or a year to get top-rated movies from that year.

## Features

- Search for movies based on year of release.
- Search for movies based on genre.
- Search for movies based on actor's name.
- Search for movies based on director's name.
- Search for movies based on creator's name.
- Broad search that considers several movie-related fields based on user queries.
- When no search results are found, the search engine attempts a fuzzy search.
- If fuzzy search also yields no results, it provides a list of top-rated movies.

## Configuration

The search engine provides configuration mode where you will be able to:

- Set the number of movies to display when a search query has been input.
- Set the fuzz ratio to specify the similarity percentage for the fuzzy search.
- Turn debug mode on for debugging

To enter this mode type `--configure` at the search prompt.

## Assumptions

Here are several key assumptions made during the development of this movie search engine:

1. **Data Quality and Structure**: The movie data is well formatted and consistent, and a movie's title and year of release uniquely identifies it. 
2. **Local Environment**: The project is run in an environment with Python 3 installed, and the user has permissions to install necessary Python packages.
3. **Python Package Availability**: Necessary Python packages (e.g., nltk, fuzzywuzzy, etc.) are readily available for download and installation via pip.
4. **Data Loading**: The data loading process is tailored to a specific file name and format. Any changes in these could necessitate modifications.
5. **Search Implementation**: The search functionality assumes the user will enter a query consisting of one or more words or possibly a year. The 'fuzzy search' assumes that a slight mismatch between searched and actual movie titles is acceptable.
6. **Configuration**: The default configuration options fit most use-cases. However, the fuzzy search ratio and other configuration options can be changed as per the requirement.
7. **Text Processing**: The removal of stop words and application of other text processing techniques (like lower casing) will improve the search results.
8. **Rating Values**: All rating values correctly reflect the quality of a movie, and a higher rated movie is generally 'better'.

## Possible Extensions

Here are several possible extensions or improvements for the movie search engine:

1. **TF-IDF Based Search**: Improve the search algorithm by using Term Frequency-Inverse Document Frequency (TF-IDF), which would refine the search by assigning weights to terms based on their importance.
2. **n-gram model**: Enhance the ability to match phrases or sequences of words using n-grams.
3. **Semantic Similarity**: Understanding semantic meanings of the words for better search results could be achieved via models like Word2Vec or Doc2Vec.
4. **Query Autocorrection**: Implement auto-correct for the user's input query leveraging libraries like PySpellChecker.
5. **Improved Ranking Algorithm**: Develop a more complex ranking algorithm that considers factors like ratings, popularity, year of release along with the relevance score.
6. **Performance Optimization**: Implement techniques to optimize search performance for large datasets; could consider using Elasticsearch for large scale applications.
7. **User Interface Upgrades**: Develop a web-based or GUI interface to improve user experience.
8. **Advanced ML Models**: Develop machine learning models for personal recommendations and advanced search results based on user's history and preferences.
9. **Speech Recognition**: Implement a voice-enabled search assistant using speech-to-text libraries.
10. **Testing**: Implement unit and integration tests.

## Contribute

If you want to contribute to this project:

1. Fork the project.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

---
Project maintained by [ayushkmr](#)
