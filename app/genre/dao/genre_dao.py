import sqlite3  # Импортируем для работы с базами данных


class GenreDAO:  # Создаём DAO для выборки по жанру

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

    def search_by_genre(self, genre):
        """
        Находит информацию о 10 самых свежих фильмах или сериалах из БД по названию жанра
        :param genre: Название жанра
        :return: Список словарей фильмов или сериалов (содержат название и описание)
        """
        db_query = f"SELECT title, description, listed_in " \
                   f"FROM {self.name} " \
                   f"ORDER BY release_year"
        db_data = self.load_database().execute(db_query).fetchall()
        searching_results_as_list = []
        for i in db_data:
            genre_list = [k.lower() for k in i[2].split(', ')]
            if genre.lower() in genre_list:
                i_dict = {"title": i[0], "description": i[1]}
                searching_results_as_list.append(i_dict)
                if len(searching_results_as_list) == 10:
                    return searching_results_as_list
        return searching_results_as_list
