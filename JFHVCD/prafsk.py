from flask import Flask
# Create the server
app = Flask(__name__)

# Root


@app.route("/")
def hello():
    return "Hello World"


if (__name__ == "__main__"):
    app.run(debug=True)

@app.route("/")
def hello():
    print("i am in hello world")
    return "<H1>Hello World</H1>"
if __name__=='__main__':
    app.run(debug=True)

