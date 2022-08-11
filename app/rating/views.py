from flask import Blueprint, jsonify  # Подключаем для создания блюпринта
from .dao.rating_dao import RatingDAO  # Импортируем для выборки фильмов и сериалов по рейтингу
from config import PATH, NAME  # Импортируем константы из конфигурационного файла

# Создаём блюпринт для выборки фильмов и сериалов по рейтингу
rating_blueprint = Blueprint("rating_blueprint", __name__)

database = RatingDAO(PATH, NAME)  # Создаём объект класса


@rating_blueprint.route("/rating/<rating>")  # Создаём эндпоинт для поиска по рейтингу
def show_movie_by_rating(rating):
    movies = database.search_by_rating(rating)
    if len(movies) == 0:
        return "Похоже, такого рейтинга нет"
    else:
        return jsonify(movies)

