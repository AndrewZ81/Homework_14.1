import sqlite3  # Импортируем для работы с базами данных


class OtherDAO:  # Создаём DAO для выборки по прочим критериям

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
        with sqlite3.connect(self.path) as db_connection:
            db_cursor = db_connection.cursor()
        return db_cursor

    def search_by_type_year_genre(self, type, year, genre):
        """
        Находит фильмы или сериалы из БД по типу, году выпуска и жанру
        :param type: Тип картины
        :param year: Год выпуска картины
        :param genre: Жанр картины
        :return: Список словарей картин (содержат название и описание)
        """
        db_query = f"SELECT title, listed_in, description " \
                   f"FROM {self.name} " \
                   f"WHERE type = '{type}'" \
                   f"AND release_year = '{year}'"
        db_data = self.load_database().execute(db_query).fetchall()
        searching_results_as_list = []
        for i in db_data:
            genre_list = [k.lower() for k in i[1].split(', ')]
            if genre.lower() in genre_list:
                i_dict = {"title": i[0], "description": i[2]}
                searching_results_as_list.append(i_dict)
        return searching_results_as_list
