from flask import Flask, flash, redirect, render_template, request, session, abort
import flask
import os

"""
http://exploreflask.com/en/latest/static.html
"""

# Static parameters
staticFiles = 'static'
app = Flask(__name__, template_folder=staticFiles)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




# Kind of distraction for protesters - not important for now.
@app.errorhandler(404)
def nonexistent_routes(error):
    # Kind of distraction for protesters - not important for now.
    #r = flask.Response(response="", status=403)
    return "<h1>404!!!!</h1>"





@app.route('/example', methods=['GET'])
def example1():
    return render_template("example1.html")


@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "About HelloFlask",
        content = "Example app page for Flask.")


# Example
@app.route('/exmaplewithparameters', methods=['POST','GET'])
def example2():
   try:
      # Get values
      v1 = str(flask.request.args.get('value1'))
      v2 = str(flask.request.args.get('value2'))
      v3 = str(flask.request.args.get('value3'))


      if len(v1) > 1 or len(v2) > 1 or len(v3) > 1:
         re = "<h1>"
         re += ("v1 is "+v1 + "<br>")
         re += ("v2 is " + v2 + "<br>")
         re += ("v3 is " + v3 + "<br>")
         re = "</h1>"
         return re
   except:
      print("Error at listening()")
      return ""


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login.html', methods=['GET'])
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('login.html')
    else:
        flask.flash('wrong password!')
        return "Wrong"
        #return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/jsexample")
def jsexample():
    return render_template('jsexmaple.html')

def main():
   try:
      app.run(host='0.0.0.0', port=8082)
   except Exception as Error:
      print(Error)
      main()

if __name__ == '__main__':
    main()

