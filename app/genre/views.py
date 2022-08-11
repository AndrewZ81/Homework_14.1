from flask import Blueprint, jsonify  # Подключаем для создания блюпринта
from .dao.genre_dao import GenreDAO  # Импортируем для выборки фильмов и сериалов по жанру
from config import PATH, NAME  # Импортируем константы из конфигурационного файла

# Создаём блюпринт для выборки фильмов и сериалов по жанру
genre_blueprint = Blueprint("genre_blueprint", __name__)

database = GenreDAO(PATH, NAME)  # Создаём объект класса


@genre_blueprint.route("/genre/<genre>")  # Создаём эндпоинт для поиска по жанру
def show_movie_by_rating(genre):
    movies = database.search_by_genre(genre)
    if len(movies) == 0:
        return "Похоже, такого жанра нет"
    else:
        return jsonify(movies)

