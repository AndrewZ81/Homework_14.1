from flask import Flask  # Импортируем для создания web-приложения
from app.title.views import movie_title_blueprint

app = Flask(__name__)  # Создаём web-приложение
app.register_blueprint(movie_title_blueprint)

if __name__ == "__main__":
    app.run()
