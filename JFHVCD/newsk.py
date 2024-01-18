from flask import Flask
app = Flask(__name__)
print('name')
@app.route('/hello')
def hello():
    return "hello to batch 4"

@app.route('/')
def hello_world():
    return'hello, world!'
if __name__=='__main__':
    app.run(debug=True)
