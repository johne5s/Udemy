from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

students = []

class Student(Resource):
    def get(self, name):
        return {'student': name}

    def post(self, name):
        student={"name":name}
        students.append(student)
        return students, 201

#these are the routes like @app.route("/")
api.add_resource(Student, '/student/<string:name>')


app.run(port=5000)