from flask import Flask
from flask_cors import CORS
from eg_blueprint import eg_blueprint

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})
app.register_blueprint(eg_blueprint)

