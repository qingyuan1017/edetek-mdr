from flask import (
    Blueprint, jsonify, request
)
from flask_restful import Api
from flaskr.resources.standard import Standard, StandardList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(StandardList, '/standards')
api.add_resource(Standard, '/standard/<string:standard_id>')
