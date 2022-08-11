import sqlite3  # Импортируем для работы с базами данных


class RatingDAO:  # Создаём DAO для выборки по рейтингу

    def __init__(self, path, name):
        """
        Создаёт атрибуты path, name
        :param path: Путь к базе данных с фильмами и сериалами (далее - БД)
        :param name: Имя БД
        """
        self.path = path
        self.name = name

    def load_database(self):
        """
        Загружает БД и создаёт указатель для неё
        :return: Указатель БД
        """
        try:
            file = open(self.path)
        except FileNotFoundError:
            quit(f"Файл {self.path} с базой данных не найден")
        else:
            file.close()
        with sqlite3.connect(self.path) as db_connection:
            db_cursor = db_connection.cursor()
        return db_cursor

    def search_by_rating(self, rating):
        """
        Находит фильмы или сериалы из БД по рейтингу
        :param rating: Рейтинг фильма или сериала
        :return: Список словарей фильмов или сериалов (содержат название, рейтинг и описание)
        """
        searching_results_as_list = []
        if rating.lower() == "children":
            db_query = f"SELECT title, rating, description " \
                       f"FROM {self.name} " \
                       f"WHERE rating = 'G'"
        elif rating.lower() == "family":
            db_query = f"SELECT title, rating, description " \
                       f"FROM {self.name} " \
                       f"WHERE rating IN ('G', 'PG', 'PG-13')"
        elif rating.lower() == "adult":
            db_query = f"SELECT title, rating, description " \
                       f"FROM {self.name} " \
                       f"WHERE rating IN ('R', 'NC-17')"
        else:
            return searching_results_as_list
        db_data = self.load_database().execute(db_query).fetchall()
        for i in db_data:
            i_dict = {"title": i[0], "rating": i[1], "description": i[2]}
            searching_results_as_list.append(i_dict)
        return searching_results_as_list
