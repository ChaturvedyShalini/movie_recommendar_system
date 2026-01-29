import requests
import json

def fetch_movie_data():
    try:
        url = "https://api.themoviedb.org/3/movie/65?api_key=537213ff06f2d2d9102ea68848e4bb38"
        headers = {
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as error:
        print(f"Error: {error}")

if _name_ == "_main_":
    fetch_movie_data()