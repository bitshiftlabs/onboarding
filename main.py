from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

class ExcuseModel(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	message = db.Column(db.String(100), nullable = False)

	def __repr__(self):
		return f"Excuse(message = {message})"




excuse_put_args = reqparse.RequestParser()
excuse_put_args.add_argument("message", type=str, help="Name of the Excuse is required", required=True)

resource_fields = {
	'id': fields.Integer,
	'message': fields.String,
}

class Excuse(Resource):
	@marshal_with(resource_fields)
	def get(self, excuse_id):
		result = ExcuseModel.query.filter_by(id = excuse_id).first()
		if not result:
			abort(404, message = "Could not find Excuse with that id ")
		return result

	@marshal_with(resource_fields)
	def put (self, excuse_id):
		args = excuse_put_args.parse_args()
		result = ExcuseModel.query.filter_by(id = excuse_id).first()
		if result:
			abort(409, message = "Excuse id taken...")
		excuse = ExcuseModel(id=excuse_id, message=args['message'])
		db.session.add(excuse)
		db.session.commit()
		return excuse, 201

api.add_resource(Excuse, "/excuse/<int:excuse_id>")

if __name__ == "__main__":
	app.run(debug=True)