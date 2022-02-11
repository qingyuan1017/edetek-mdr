from flask_restful import Resource, reqparse, marshal_with, fields
from flaskr.db import get_db, close_db
from flaskr import schema

standard_list_serializer = {'id': fields.Integer, 'name': fields.String, 'description':
    fields.String}


class StandardList(Resource):
    @marshal_with(standard_list_serializer)
    def get(self):
        try:
            rows = schema.Standard.query.all()
            return rows
        except Exception as e:
            print(e)
        finally:
            close_db()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name')
            parser.add_argument("description")
            args = parser.parse_args()
            _name = args['name']
            _description = args['description']

            post_standard = schema.Standard(name=_name, description=_description)
            db = get_db()
            db.session.add(post_standard)
            db.session.commit()
            return "hello world"

        except Exception as e:
            print(str(e) + "error")
        finally:
            close_db()


class Standard(Resource):
    @marshal_with(standard_list_serializer)
    def get(self, standard_id):
        try:
            print(standard_id)
            rows = schema.Standard.query.get(standard_id)
            return rows
        except Exception as e:
            print(e)
        finally:
            close_db()

    def delete(self, standard_id):
        try:
            db = get_db()
            delete_standard = schema.Standard.query.filter_by(id=standard_id)
            db.session.delete(delete_standard)
            db.session.commit()

        except Exception as e:
            print(e)
        finally:
            close_db