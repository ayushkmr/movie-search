from src.utils.utils import load_movies_from_json_file


def main():
    # Specify the path to your JSON file
    json_filepath = "movies.json"
    
    # Load JSON data from file into Movie objects
    movies = load_movies_from_json_file(json_filepath)
    
    # Print total number of movies loaded
    print(f"Total {len(movies)} movies loaded from JSON file.")


if __name__ == "__main__":
    main()