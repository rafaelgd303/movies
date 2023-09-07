from tmdb_client import get_movies, get_popular_movies, get_poster_url, get_single_movie, get_single_movie_cast, get_list_of_movies
from flask import Flask, render_template, request


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    user_list_type = request.args.get('list_type')
    list_of_movies = get_list_of_movies()
    if user_list_type not in list_of_movies:
        user_list_type = "popular"
    # selected_list = request.args.get('list_type', "popular")
    movies = get_movies(how_many=8, list_type=user_list_type)
    return render_template("homepage.html", movies=movies, current_list=user_list_type, list_of_movies=list_of_movies)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = get_single_movie(movie_id)
    cast = get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)
