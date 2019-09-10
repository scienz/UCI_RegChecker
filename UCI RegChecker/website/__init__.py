from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = '25f1cc7613ddd69e9c60ffda3345fc58'

from website import routes
