import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


# @app.route('/hello', methods=['POST'])
# def hello():
#     name = request.form.get('name')
#     return render_template('hello.html', name = name)


if __name__ == '__main__':
   app.run()
