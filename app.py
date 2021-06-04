from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hi')
def hi():
    return "Hi /user"

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    #get x,y from the posted data
    data = request.get_json()

    if 'y' not in data:
        return "ERROR", 305
    x = data['x']
    y = data['y']

    # add z = x+ y
    z = x + y

    # prepare a json "z":z
    restD = {
        'z': z
    }
    # return jsonify(map_prepared)
    return jsonify(restD), 200

@app.route('/bye')
def bye():
    c = 223*4
    s = str(c)
    # a = 1/0
    resltData = {
        'name': 'sonu',
        'age': 27,
        'phone':[
           {
            'phone_name': 'phone 1',
            'phone_no': 8819888
           },
            {
            'phone_name': 'phone 2',
            'phone_no': 988654
           }
        ]
    }
    return jsonify(resltData)


if __name__=="__main__":
    app.run(host="127.0.0.1", port=8009, debug=True)