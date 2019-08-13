import json

from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory
import flask
import os
import requests


"""
http://exploreflask.com/en/latest/static.html
"""

# Static parameters
staticFiles = 'static'
app = Flask(__name__, template_folder=staticFiles)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
authServer = '127.0.0.1'


@app.route('/', methods=['GET'])
def root():
    return Clearview()

@app.route('/Clearview', methods=['GET'])
def Clearview():
    return render_template("Clearview.html")

@app.route('/Shop', methods=['GET'])
@app.route('/Shop?', methods=['GET'])
def shop():
    statement, response = isAuthorized(request)
    if statement:
        json_data = json.loads(response.text)
        username = json_data['username']
        email = json_data['email']
        role = json_data['role']['name']

        return render_template("Authorized_Shop.html", username=username, email=email, role=role)
    return render_template("Shop.html")

@app.route('/essentials', methods=['GET'])
def essentials():
    return render_template("essentials.html")

@app.route('/foundation', methods=['GET'])
def foundation():
    return render_template("foundation.html")

@app.route('/haven', methods=['GET'])
def haven():
    return render_template("haven.html")

@app.route('/knox', methods=['GET'])
def knox():
    return render_template("knox.html")




# Auth functions

def isAuthorized(request):
    if 'AUTH' in request.cookies:
        # validate
        token = request.cookies['AUTH']
        Authorization = 'Bearer ' + token
        headers = {'Authorization': Authorization}
        response = requests.get('http://'+authServer+':1337/users/me',
                         headers=headers,
                         verify=False)
        if response.status_code == 200:
            return True, response
        return False, response
    else:
        return False, None







# Kind of distraction for protesters - not important for now.
@app.errorhandler(404)
def nonexistent_routes(error):
    # Kind of distraction for protesters - not important for now.
    #r = flask.Response(response="", status=403)
    return "<h1>404!!!!</h1>"

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)

# Check this
@app.route('/favicon.ico')
def send_ico():
    return render_template("/images/favicon.ico")


def main():
   try:
      app.run(host='0.0.0.0', port=8088)
   except Exception as Error:
      print(Error)
      main()

if __name__ == '__main__':
    main()

