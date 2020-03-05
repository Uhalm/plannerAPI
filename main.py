from flask import Flask, request, jsonify
import datetime
import json

#globals
app = Flask(__name__)
save_data = {}
school = 'hold'

#Main page to send test data to the client
@app.route("/")
def index():
    return "<h1> The Current Time On The Server Is ERROR NO TIME AVALIBLE</h1>"

#initalize the server when it is first booted
@app.route("/init", methods=['GET'])
def server_init():
    global school
    school = classes()
    code = server_start()
    return code

#Send the actual data to the client
@app.route("/dataInteract", methods=['GET'])
def get_data():
    save_data = data_load()
    return save_data

#Get new data from the client
@app.route("/dataInteract", methods=['POST'])
def post_data():
    data = request.args
    print(jsonify(data))
    if data != "":
        return "201"
    else:
        return "200"

#Delete data the client wants deleted
@app.route("/dataInteract", methods=['DELETE'])
def delete_data():
    pass

def data_load():
    global save_data
    save_data = json.load(open('savedData.json'))
    return save_data

def server_start():
    global school
    json_data = data_load()
    for x in range(1, 8):
        if x == 1:
            school.a.name = json_data['a']['name']
            school.a.assignment = json_data['a']['assignment']

        elif x == 2:
            school.b.name = json_data['b']['name']
            school.b.assignment = json_data['b']['assignment']

        elif x == 3:
            school.c.name = json_data['c']['name']
            school.c.assignment = json_data['c']['assignment']

        elif x == 4:
            school.d.name = json_data['d']['name']
            school.d.assignment = json_data['d']['assignment']
        
        elif x == 5:
            school.e.name = json_data['e']['name']
            school.e.assignment = json_data['e']['assignment']

        elif x == 6:
            school.f.name = json_data['f']['name']
            school.f.assignment = json_data['f']['assignment']

        elif x == 7:
            school.g.name = json_data['g']['name']
            school.g.assignment = json_data['g']['assignment']
        
        else:
            print("ERROR you fucked up the code somewhere this is on line 69 btw")
    
    return '200'
        


class classes(object):
    class a(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment
    
    class b(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment

    class c(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment
    
    class d(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment

    class e(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment

    class f(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment

    class g(object):
        def __init__(self, name, assignment):
            self.name = name
            self.assignment = assignment




if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)