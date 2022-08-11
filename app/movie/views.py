from flask import Blueprint, jsonify  # Подключаем для создания блупринта
from .dao.movie_dao import TitleDAO  # Импортируем для выборки по названиям
from config import PATH, NAME

movie_title_blueprint = Blueprint("movie_title_blueprint", __name__, url_prefix="/movie")
database = TitleDAO(PATH, NAME)


@movie_title_blueprint.route("/<title>")
def show_movie_by_title(title):
    movie = jsonify(database.search_by_title(title))
    return movie
