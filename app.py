from flask import Flask
from app.title.dao.title_dao import TitleDAO

app = Flask(__name__)
app.config.from_pyfile("config.py")
db_path = app.config.get("PATH")
db_name = app.config.get("NAME")

database = TitleDAO(db_path, db_name)

if __name__ == "__main__":
    app.run()
