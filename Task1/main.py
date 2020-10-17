from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import random, requests

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

class ExcuseModel(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	message = db.Column(db.String(100), nullable = False)

	def __repr__(self):
		return f"Excuse(message = {message})"

db.create_all()


excuse_put_args = reqparse.RequestParser()
excuse_put_args.add_argument("message", type=str, help="Name of the Excuse is required", required=True)


excuse_update_args = reqparse.RequestParser()
excuse_update_args.add_argument("message", type=str, help="Name of the Excuse is required", required=True)


resource_fields = {
	'id': fields.Integer,
	'message': fields.String,
}

BASE = "http://127.0.0.1:5000/"

# This is already set up in the database this is for visualization purpose.
data = [{ "message": "My dog is throwing up" },
		{ "message": "I have some  work" },
		{ "message": "I have a package I have to sign for" },
		{ "message": "OMG I totally forgot we had plans" },
		{ "message": "I had a stomach full meal I can't move " },
		{ "message": "I totally missed this!" },
		{ "message": "I haven't finished planning yet" },
		{ "message": "It's a work in progress" },
		{ "message": "I've got too many urgent things to do " },
		{ "message": "I Dont have permission" },
		{ "message": "I'm not feeling well" },
		{ "message": "I have work tonight" },
		{ "message": "I have work early tomorrow" },
		{ "message": "Oh, was that tonight" },
		{ "message": "There's a pet emergency " },
		]

@app.route('/excuse',methods=['GET'])
def display():
	title ="Excuse"
	n = random.randint(0,len(data)-1)
	response = requests.get(BASE+"excuse/"+str(n))
	return response.json()


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

	@marshal_with(resource_fields)
	def patch(self, excuse_id):
		args = excuse_update_args.parse_args()
		result = ExcuseModel.query.filter_by(id = excuse_id).first()
		if not result:
			abort(404, message = "Excuse doesn't exist... , cannot update ")
		if args['message']:
			result.message = args['message']

		db.session.commit()

		return result


api.add_resource(Excuse, "/excuse/<int:excuse_id>")

if __name__ == "__main__":
	app.run(debug=True)
