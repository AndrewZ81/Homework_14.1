import sqlite3

with sqlite3.connect("data/netflix.db") as netflix_connection:
    netflix_cursor = netflix_connection.cursor()
netflix_query = """
                   SELECT title, country FROM netflix LIMIT 10
                """
netflix_data = netflix_cursor.execute(netflix_query).fetchall()
