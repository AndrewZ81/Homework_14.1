from flask import Blueprint, jsonify  # Подключаем для создания блюпринта
from .dao.movie_dao import MovieDAO  # Импортируем для выборки фильмов и сериалов по названиям и годам выпуска
from config import PATH, NAME  # Импортируем константы из конфигурационного файла

# Создаём блюпринт для выборки фильмов и сериалов по названиям и годам выпуска
movie_blueprint = Blueprint("movie_blueprint", __name__, url_prefix="/movie")

database = MovieDAO(PATH, NAME)  # Создаём объект класса


@movie_blueprint.route("/<title>")  # Создаём эндпоинт для поиска по названию
def show_movie_by_title(title):
    try:
        movie = jsonify(database.search_by_title(title))
    except IndexError:
        return "Похоже, такого фильма или сериала нет"
    else:
        return movie


# Создаём эндпоинт для поиска по годам выпуска
@movie_blueprint.route("/<int:from_year>/to/<int:to_year>")
def show_movies_by_years(from_year, to_year):
    movies = database.search_by_years(from_year, to_year)
    if len(movies) == 0:
        return "Похоже, таких фильмов или сериалов нет"
    else:
        return jsonify(movies)
