from config import PATH, NAME  # Импортируем константы из конфигурационного файла
from other_dao import OtherDAO # Импортируем для выборки поиск картин из БД по типу, году выпуска и жанру


try:
    file = open(PATH)
except FileNotFoundError:
    quit(f"Файл {PATH} с базой данных не найден")
else:
    file.close()

# Вызываем поиск картин из БД по типу, году выпуска и жанру
database = OtherDAO(PATH, NAME)  # Создаём объект класса

# Создаём тесты
unreal_pictures = database.search_by_type_year_genre("Movie", 1000, "Dramas")
real_pictures = database.search_by_type_year_genre("Movie", 2000, "Dramas")

try:
    assert unreal_pictures == [], "Картины в 1000 г. вообще не снимали!"
    assert real_pictures != [], "Картины этого жанра в 2000 г. снимали!"
except AssertionError:
    print("Поиск картин из БД по типу, году выпуска и жанру работает некорректно")
    raise
else:
    print("Поиск картин из БД по типу, году выпуска и жанру работает корректно")