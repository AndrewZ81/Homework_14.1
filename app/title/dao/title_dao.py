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

    def get_database(self):
        """
        Возвращает БД в форме списка
        :return: БД в форме списка
        """
        db_query = f"SELECT title, country FROM {self.name} LIMIT 10"
        db_data = self.load_database().execute(db_query).fetchall()
        return db_data
