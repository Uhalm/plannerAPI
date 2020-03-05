#Import the flask modules
from flask import Flask, jsonify, session, render_template, abort, request, redirect, url_for, make_response
from flask_login import current_user, login_required, LoginManager
import objects

#set the globals
app = Flask(__name__)
app.secret_key = 'key123'

#Render the login page at /
@app.route('/', methods=['GET'])
def login():
    return render_template("login.html")

#Do this when data is posted to /
@app.route('/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    session['uuid'] = username
    if username != " " and password != " ":
        return redirect(url_for('dashboard_main', uuid=username.capitalize()))
    else:
        return render_template('login.html')

#Redner the dashboard with a uuid
@app.route('/dashboard/<uuid>', methods=['GET'])
def dashboard_main(uuid):
    return render_template("dashboard.html", uuid=uuid)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('uuid', None)
    return redirect(url_for('login'))

def on_start():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)