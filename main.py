from flask import Flask  # Импортируем для создания web-приложения
from app.movie.views import movie_blueprint  # Импортируем блюпринт для поиска по годам и названию
from app.rating.views import rating_blueprint  # Импортируем блюпринт для поиска по рейтингу
from app.genre.views import genre_blueprint  # Импортируем блюпринт для поиска по жанру

app = Flask(__name__)  # Создаём web-приложение
app.config.from_pyfile("config.py")

try:
    db_path = app.config.get("PATH")
    file = open(db_path)
except FileNotFoundError:
    quit(f"Файл {db_path} с базой данных не найден")
else:
    file.close()
    app.register_blueprint(movie_blueprint)  # Регистрируем блюпринты
    app.register_blueprint(rating_blueprint)
    app.register_blueprint(genre_blueprint)
    if __name__ == "__main__":
        app.run()
