from flask import Flask, jsonify, request
from flask_restful import  Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, fuctionName):
    if (fuctionName == 'add'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        # if i am here then the resource add was requested using the method post
        
        # step 1 : get posted data:
        postedData = request.get_json()

        # step 1.2 verify validity of posted data
        status_code = checkPostedData(postedData, 'add')
        if (status_code!=200):
            retJson = {
                "Message": "An error happened!",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # if i am here, then status_code == 200
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # step 2: add the posted data
        rest = x + y
        restJson = {
            'message': rest,
            'code': 200
        }
        return jsonify(restJson)

class subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, '/add')

@app.route('/')
def hello_world():
    return "Hello World 2!"

if __name__=="__main__":
    app.run()