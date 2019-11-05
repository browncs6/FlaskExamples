from flask import Flask, abort, request, make_response

app = Flask(__name__)

# define routes here
@app.route('/')
def index():
    return '<h1>Hello world</h1>'


# we can use parts of URIs as variables
@app.route('/blog/<int:year>/<int:month>/<string:title>')
def blog(title, month, year):
    return '<h1>{}</h1><h3>{}/{}</h3><p>An important story is written here...</p>'.format(title, month, year)


# returning bad status codes
@app.route('/404')
def make404():
    return 'This page yields a 404 error', 404

# returning bad status codes
@app.route('/alsobad')
def makeAnotherBadRoute():
    abort(404)

@app.errorhandler(404)
def notfound(error):
    return "<h1>HTTP NOT FOUND ERROR</h1><p>{}</p>".format(error)

@app.route('/csv')
def csv():
    return app.response_class(response='a,b,c\n1,2,3\n4,5,6', mimetype='text/csv')


@app.route('/get', methods=['GET'])
def get_route():
    response = '<p>{} request {} issued<p><p>' \
               'Headers<br>{}</p>' \
               '<p>Query args:<br>{}'.format(request.method,
                                             request.full_path,
                                             request.headers,
                                             request.args)
    return response, 200

@app.route('/post', methods=['POST'])
def post_route():
    # test via curl -sD - --form 'name=tux' --form 'profession=penguin' http://localhost:5000/post

    print(request.form)
    body = '<table>'
    for k, v in request.form.items():
        body = '<tr><td>{}</td><td>{}</td></tr>'.format(k, v)
    body += '</table>'

    response = make_response(body)
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response

if __name__ == '__main__':
    # use debug=True to autoreload changes in code
    app.run(debug=True)
