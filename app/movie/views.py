from flask import Blueprint, jsonify  # Подключаем для создания блюпринта
from .dao.movie_dao import MovieDAO  # Импортируем для выборки фильмов и сериалов по названиям и годам выпуска
from config import PATH, NAME

movie_blueprint = Blueprint("movie_blueprint", __name__, url_prefix="/movie")
database = MovieDAO(PATH, NAME)


@movie_blueprint.route("/<title>")
def show_movie_by_title(title):
    movie = jsonify(database.search_by_title(title))
    return movie


@movie_blueprint.route("/<int:from_year>/to/<int:to_year>")
def show_movies_by_years(from_year, to_year):
    movies = jsonify(database.search_by_years(from_year, to_year))
    return movies
