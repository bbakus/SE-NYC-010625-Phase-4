#!/usr/bin/env python3

from flask import Flask
from flatburger.data import burgers
from flatburger.html import flatburger_html_code



app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to my website</h1>'

@app.route('/another')
def different():
    return f'<h2>I love anal sex</h2>'

@app.route('/intro/<name>')
def intro(name):
    return f'<h2>Hi my name is {name}</h2>'

@app.route('/intro/<name>/<int:age>')
def intro_2(name, age):
    return f'<h1>My name is {name}, and I am {age} years old.'

@app.route('/<float:number>')
def float(number):
    return f'I give {number} fucks'


#deliverable number 1 solution code

@app.route('/greeting/<first_name>/<last_name>')
def greeting(first_name, last_name):
    return f'<h1>Greetings {first_name} {last_name}.</h1>'


#deliverable 2

@app.route('/count_and_square/<int:number>')
def count_and_square(number):
    squared_num_string = ""

    for num in range(1, number + 1):
        squared_num_string += f"{num ** 2}\n"

    return squared_num_string


#deliverable #3

@app.route('/burgers')
def get_burgers():
    return burgers


#deliverable 4

@app.route('/flatburger_page')
def flatburger():
    return flatburger_html_code

if __name__ == "__main__":
    app.run(port=7777, debug=True)
