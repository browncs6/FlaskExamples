from flask import Flask

app = Flask(__name__)

# define routes here
@app.route('/')
def index():
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run()
