import media
import fresh_tomatoes
import json
import requests


def get_video_url(movie_id, api_key):
    """
    Takes in Movie Id and api key, and finds the video URL related to movie.
    """
    MOVIE_URL = "https://api.themoviedb.org/3/movie/"
    LANG = "&language=en-US"

    # Append youtube URL to the key
    VIDEO_URL_START = "https://www.youtube.com/watch?v="

    # Find the key from TMDB
    connection = requests.get(MOVIE_URL + str(movie_id) +
                              "/videos?api_key=" + api_key + LANG)
    parsed_json = json.loads(connection.text)
    connection.close()

    # Return Result
    return VIDEO_URL_START + parsed_json['results'][0]['key']


def get_movie_object_given_dict(movie_data_dict, api_key, img_url_start):
    """
    Takes the result movie dictionary and api key along with image url to
    start and returns the movie object relate to dictionary.
    """

    title = movie_data_dict['title']
    story_line = movie_data_dict['overview']
    img_url = img_url_start + movie_data_dict['poster_path']
    video_url = get_video_url(movie_data_dict['id'], api_key)

    return media.Movie(title, story_line, img_url, video_url)


def get_movies_objects_list(search_url, api_key, query_append,
                            img_url, query_list):
    """
    Connects to TMDB Api with given API key and search url and generates
    the movie data list.
    """
    movies = []
    for i in range(len(query_list)):
        connection = requests.get(search_url + api_key +
                                  query_append + movies_list[i])
        parsed_json = json.loads(connection.text)
        connection.close()
        if len(parsed_json['results']) == 0:
            print("Not found '" + " ".join(movies_list[i].split('+')) +
                  "' movie..No Worries Skipping it.")
            continue
        result_dict = parsed_json['results'][0]
        movies.append(get_movie_object_given_dict(result_dict,
                      api_key, img_url))
    return movies


if __name__ == '__main__':
    # Take Movies input to include them in Site
    movies_list = []

    num_of_movies = int(input("Enter the number of movies: "))

    # make sure to convert input in form of + join rather than space join
    # example if input is "Iron Man" convert it to "Iron+Man" to send it
    # in search query
    for i in range(num_of_movies):
        movies_list.append("+".join(input("Enter Movie: ").split()))

    # Constants for Search and Image URLS
    IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    SEARCH_URL = "https://api.themoviedb.org/3/search/movie?api_key="
    API_KEY = input('Enter API KEY from "https://www.themoviedb.org/": ')
    QUERY_APPEND = "&query="

    # Get List of Movie Objects
    movies = get_movies_objects_list(SEARCH_URL, API_KEY, QUERY_APPEND,
                                     IMAGE_URL, movies_list)

    # Generate Web Page
    fresh_tomatoes.open_movies_page(movies)
