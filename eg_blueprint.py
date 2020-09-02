from flask import Blueprint, request, url_for, Response, jsonify

eg_blueprint = Blueprint('eg_blueprint', __name__)

@eg_blueprint.route('/', methods=['POST'])
def fetchdata():
    list = [{"service":"Blood Pressure","price":"20"}, {"service":"Blood Sugar","price":"30"}]
    return jsonify(list)