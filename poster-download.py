import requests
import json
import os

# Your JSON data
data = [
    
    {
        "title": "Gangs of Wasseypur",
        "releaseYear": "2012",
        "genre": "Action, Comedy, Crime",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BMTc5NjY4MjUwNF5BMl5BanBnXkFtZTgwODM3NzM5MzE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "Lagaan",
        "releaseYear": "2001",
        "genre": "Drama, Musical, Sport",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BNDYxNWUzZmYtOGQxMC00MTdkLTkxOTctYzkyOGIwNWQxZjhmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "Rang De Basanti",
        "releaseYear": "2006",
        "genre": "Comedy, Crime, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BYThmZDA0YmQtMWJhNy00MDQwLTk0Y2YtMDhmZTE5ZjhlNjliXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "Mughal-E-Azam",
        "releaseYear": "1960",
        "genre": "Drama, Romance, War",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BMmM2YWQ3MzctOTk1NS00NThhLWExY2MtYjQzZGRmZTFiYWY3XkEyXkFqcGdeQXVyMjUxMTY3ODM@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "3 Idiots",
        "releaseYear": "2009",
        "genre": "Comedy, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "Sardar Udham",
        "releaseYear": "2021",
        "genre": "Biography, Crime, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BZGFhNTYwZmMtNzk4Ny00MTExLThjMWUtNjYzMTEwZjEzMWQ3XkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "The Shawshank Redemption",
        "releaseYear": "1994",
        "genre": "Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "The Godfather",
        "releaseYear": "1972",
        "genre": "Crime, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "title": "Pulp Fiction",
        "releaseYear": "1994",
        "genre": "Crime, Drama",
        "coverUrl": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg"
    }
]

# Create a directory named 'Movie_Posters' if it doesn't exist
if not os.path.exists('Movie_Posters'):
    os.makedirs('Movie_Posters')

for movie in data:
    image_url = movie['coverUrl']
    title = movie['title'].replace(' ', '_')  # Replace spaces with underscores
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open file in binary mode and write into it
        with open(os.path.join('Movie_Posters', f"{title}.jpg"), 'wb') as file:
            file.write(response.content)


