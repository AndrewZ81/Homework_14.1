from flask import Blueprint, jsonify  # Подключаем для создания блупринта
from .dao.title_dao import TitleDAO  # Импортируем для выборки по названиям
from config import PATH, NAME

movie_title_blueprint = Blueprint("movie_title_blueprint", __name__)
database = TitleDAO(PATH, NAME)


@movie_title_blueprint.route("/movie/<title>")
def show_movie_by_title(title):
    movie = database.search_by_title(title)
    return jsonify(movie)
