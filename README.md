# Movie Search Engine

A command-line based movie search engine that allows users to search for movie names based on one or several words related to the movie. The search engine also has the ability to display a list of the top-rated movies when no search results are found.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contribute](#contribute)

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

You will be prompted to enter a search query. You can enter a single keyword or multiple keywords to search for movies. 

If you want to enter configuration mode, enter `--configure`.

In configuration mode, you will be able to:

- Set the number of movies to display when a search query has been input.
- Set a custom message to display when no search results are found.

## Features

- Search movie names based on user queries.
- Allows configuration for the number of search results and the message to display when no results are found.
- Provides top-rated movies when no search results are found.

## Contribute

If you want to contribute to this project:

1. Fork the project.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.


---
Project maintained by [ayushkmr](#)
