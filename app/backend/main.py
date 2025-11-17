# starting point for database's Flask API
# note: not sure exactly where to go from here

from flask import Flask
from postgres_login import login
from chunking import wine_data_extraction, chunk_text

app = Flask(__name__)


@app.route("/")
def root_route():
    print("start of route")
    return


if __name__ == "__main__":
    cursor = login()
    data = wine_data_extraction()
