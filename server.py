from flask import Flask, request;
from flask_restful import Resource, Api, reqparse;
from sqlalchemy import create_engine;
#from flask.ext.jsonpfiy import jsonify
import json;



#db_connect = create_engine('sqlite:///')
app = Flask(__name__);
api = Api(app);


users = [
	{
		"name": "Paul",
		"age": "16",
		"occupation": "CEO"
	},
	{
		"name": "Nick",
		"age": "16",
		"occupation": "Head of Music"
	},
	{
		"name": "Josh",
		"age": "17",
		"occupation": "Head of Development"
	}
]


homework = [
	{
		"subject": "ASL",
		"period": "A",
		"work": "NUL"
	},
	{
		"subject": "Economics",
		"period": "B",
		"work": "NUL"
	},
	{
		"subject": "AP Art - Photo",
		"period": "C",
		"work": "NUL"
	},
	{
		"subject": "Theology",
		"period": "D",
		"work": "NUL"
	},
	{
		"subject": "Composition",
		"period": "E",
		"work": "NUL"
	},
	{
		"subject": "Physics",
		"period": "F",
		"work": "NUL"
	},
	{
		"subject": "Algebra",
		"period": "G",
		"work": "NUL"
	}

]



print('running');

class test(Resource):
	def get(self):
		return 'test succsessful'


class index(Resource):
	def get(self):
		ver = '0.0.2';
		user = 'Uhalm';
		password = 'hash';
		data = 'ver:', ver, 'user:', user, 'password:', password
		return data;


class planner(Resource):

	def get(self, subject):
		for work in homework:
			if(subject == work["subject"]):
				return work, 200;
		return "No you get 404", 404;


	def post(self, subject):
		parser = reqparse.RequestParser();
		parser.add_argument("period");
		parser.add_argument("work");
		args = parser.parse_args();

		for work in homework:
			if(subject == work["subject"]):
				return "That subject exists... plus why the fuck are you adding a subject you shouldnt change this";

		work = {
			"subject": subject,
			"period": args["period"],
			"work": args["work"]
			}

		homework.append(work);
		return work, 201;

	def put(self, subject):
		parser = reqparse.RequestParser();
		parser.add_argument("period");
		parser.add_argument("work");
		args = parser.parse_args();

		for work in homework:
			if(subject == work["subject"]):
				work["period"] = args["period"];
				work["work"] = args["work"];
				return work, 200;

		work = {
			"subject": subject,
			"period": args["period"],
			"work": args["work"]
			}
		homework.append(work);
		return work, 201;
"""

	def delete(self):

"""

class User(Resource):

	def get(self, name):
		for user in users:
			if(name == user["name"]):
				return user, 200;
		return "User not found", 404;

	def post(self, name):
		parser = reqparse.RequestParser();
		parser.add_argument("age");
		parser.add_argument("occupation");
		args = parser.parse_args();

		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400;

		user={
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
			}
		users.append(user);
		return user, 201;

	def put(self, name):
		parser = reqparse.RequestParser();
		parser.add_argument("age");
		parser.add_argument("occupation");
		args = parser.parse_args();

		for user in users:
			if(name == user["name"]):
				user["age"] = args["age"];
				user["occupation"] = args["occupation"];
				return user,200;

		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
			}

		users.append(user)
		return user, 201

	def delete(self, name):
		global users
		users = [user for user in users if user["name"] != name]
		return "{} is deleted.".format(name), 200;


api.add_resource(test, '/test');
api.add_resource(index, '/index');
#api.add_resource(User, '/users/<string:name>');
api.add_resource(User, '/users/<string:name>');
api.add_resource(planner, '/planner/<string:subject>');


if __name__ == '__main__':
	app.run(port='5002', debug=True);
