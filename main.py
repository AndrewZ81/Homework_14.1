from flask import Flask  # Импортируем для создания web-приложения
from app.movie.views import movie_blueprint  # Импортируем блюпринт для поиска по годам и названию

app = Flask(__name__)  # Создаём web-приложение
app.register_blueprint(movie_blueprint)

if __name__ == "__main__":
    app.run()
