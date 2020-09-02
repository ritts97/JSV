from flask import Flask
from eg_blueprint import eg_blueprint

app = Flask(__name__)
app.register_blueprint(eg_blueprint)

