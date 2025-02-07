from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_date():
    dt = datetime.now()
    dt_format = dt.strftime("%d/%m/%y")
    return "Привет, Максим! Текущая дата: {}".format(dt_format)


if __name__ == "__main__":
    app.run()
