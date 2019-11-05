#!/usr/bin/env python3
# This example demonstrates how to serve
# static files via Flask

from flask import Flask, render_template, request, abort
import random

app = Flask(__name__)

# define here routes
@app.route('/')
def index():
    return render_template('index.html', first_operand=random.randint(0, 10), second_operand=random.randint(0, 10))

@app.route('/calc', methods=['POST'])
def calc():
    res = 'undefined'

    op1 = int(request.form['first_operand'])
    op2 = int(request.form['second_operand'])
    op = request.form['operator']

    if op == '+':
        res = op1 + op2
    elif op == '-':
        res = op1 - op2
    elif op == '*':
        res = op1 * op2
    elif op == '/':
        res = op1 / op2
    else:
        abort(404)
    return render_template('calc.html',
                           first_operand = op1,
                           second_operand = op2,
                           operator=op,
                           result=res)


if __name__ == '__main__':
    # add debug = True to auto reload templates
    # during development
    app.run(debug=True)
