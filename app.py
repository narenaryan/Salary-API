'''
12/23/16 (bolbs in ny; we walked to barclay center/fulton mall last night and ate at pizzeria; hes still a boy in many ways; 1st week back after two weeks of offsites and leadership training; watching david attenboruoughs trials of life - one of the best series ive seen; doing a lot of random things at work - perch/smartthings, marketing spend, lotik modeling, etc. i actually like it; walked to office todya and picked up turtlebot; want to spend more time with ros and robotics; bay fell asleep at 6ish - shes been through a lot after fran and lydia both left; coding at maple now - bolbs/laura/lurm went ice skating; will go to peter luger later; bay is feeling a bit disconnected since ive been gone for so long but i think we're both tired and busy with work; reviewing restful apis so i can actually have a convo with adrian)


3/18/17 (emily to be gone for two weeks; lurm is back from sxsw; trying to hire yukuan but shana is getting in the way; in a good space with bay right now as long as we talk; long week for both of us due to work; trying to bring stae over the finish line; at lpq now there are so many screaming babies; ben su got a new job; bolbs laura in thailand for edisons wedding; did a metis presentation yesterday; saw ben yesterday; angela is moving to paris; juyoung is imploding and will move to lotik; mike park in town for spring break - itll be nice to see him and talk abotu science; thinking about going to copahagen with my beautiful wife; reviewing api's because im researching api fortress as a potential investment)
'''

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///salaries.db')  # loads db into memory

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

class Departments_Meta(Resource):
	def get(self):
		conn = e.connect()  # open connection to memory data
		query = conn.execute("select distinct DEPARTMENT from salaries")  # query
		return {'departments': [i[0] for i in query.cursor.fetchall()]}  # format results in dict format

class Departmental_Salary(Resource):
    def get(self, department_name):  # param is pulled from url string
    	conn = e.connect()
    	query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class multiply(Resource):
    '''dummy function to test apis'''
    def get(self, number):  # param must match uri identifier
        return number * 2

# once we've defined our api functionalities, add them to the master API object
api.add_resource(Departments_Meta, '/departments')  # bind url identifier to class
api.add_resource(Departmental_Salary, '/dept/<string:department_name>')  # bind url identifier to class; also make it querable
api.add_resource(multiply, '/multiply/<int:number>')  # whatever the number is, multiply by 2

if __name__ == '__main__':
    app.run(debug=True)