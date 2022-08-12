from config import PATH, NAME  # Импортируем константы из конфигурационного файла
from other_dao import OtherDAO # Импортируем для выборки поиск картин из БД по типу, году выпуска и жанру

try:
    file = open(PATH)
except FileNotFoundError:
    quit(f"Файл {PATH} с базой данных не найден")
else:
    file.close()

database = OtherDAO(PATH, NAME)  # Создаём объект класса

# Вызываем поиск картин из БД по типу, году выпуска и жанру в виде тестов
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

# Вызываем поиск акиёров из БД, сыгравших с данными актёрами более двух раз
real_actors = database.search_by_actors("Rose McIver", "Ben Lamb")
unreal_actors = database.search_by_actors("Unreal Actor", "Unreal Actor")

try:
    assert unreal_actors == [], "Не ни одного актёра, сыгравших с данными актёрами более двух раз!"
    assert real_actors != [], "Есть актёры, сыгравшие с данными актёрами более двух раз!"
except AssertionError:
    print("Поиск актёров из БД, сыгравших с данными актёрами более двух раз, работает некорректно")
    raise
else:
    print("Поиск актёров из БД, сыгравших с данными актёрами более двух раз, работает корректно")
