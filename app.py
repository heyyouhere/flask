from flask import *

app = Flask(__name__)

data = {'start' : 'end'}

@app.route('/')
def foo():
    return render_template('index.html')


@app.route('/result')
def bar():
    return jsonify(data)


@app.route('/api', methods=['POST'])
def post():
    if request.headers.get('Content-Type') == 'application/json':
        print(request.json.get('hello'))
        return jsonify({'OK' : '200'})
    return "Record not found", 400

app.run()
