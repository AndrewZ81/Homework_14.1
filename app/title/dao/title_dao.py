import sqlite3  # Импортируем для работы с базами данных


class TitleDAO:  # Создаём DAO для выборки по названиям

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

    def search_by_title(self, title):
        """
        Находит информацию о самом свежем фильме или сериале из БД по запросу
        :param title: Название фильма или сериала запроса
        :return: Словарь подробной информации о фильме или сериале БД из запроса
        """
        db_query = f"SELECT title, country, release_year, listed_in, description FROM {self.name}"
        db_data = self.load_database().execute(db_query).fetchall()
        searching_results_as_tuple = ()
        last_year = 0
        for i in db_data:
            if title.lower() == i[0].lower():
                if i[2] > last_year:
                    searching_results_as_tuple = i
                    last_year = i[2]
        searching_results_as_dict = {"title": searching_results_as_tuple[0],
                             "country": searching_results_as_tuple[1],
                             "release_year": searching_results_as_tuple[2],
                             "genre": searching_results_as_tuple[3],
                             "description": searching_results_as_tuple[4]}
        return searching_results_as_dict
