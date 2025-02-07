from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_date():
    dt = datetime.now()
    dt_format = dt.strftime("%d/%m/%y")
    return "Hello, Maksim!"


if __name__ == "__main__":
    app.run()
