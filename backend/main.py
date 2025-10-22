# starting point for database's Flask API
# note: not sure exactly where to go from here

from flask import Flask

app = Flask(__name__)


@app.route("/")
def root_route():
    print("start of route")
    return


if __name__ == "__main__":
    print("start of program")
