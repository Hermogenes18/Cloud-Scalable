from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
   return 'welcome'

def do_the_login():
    return 'This was a POST request'

def show_the_login_form():
    return 'Not POST. Are you GETting me? :)'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == "__main__":
    app.run(debug=True)