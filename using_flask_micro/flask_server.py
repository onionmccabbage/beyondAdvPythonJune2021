# this file is often called app.py

from flask import Flask # we may need to pip install flask
from flask import render_template
import json

# we begin by declaring our flask app
app = Flask(__name__) # we now have a microservice called app
app.debug=True # make this a listening server

# declare routes for our app
@app.route('/') # this is the ROOT of our service
def root(): # name of route matches purpose
    content = '''
    <h1>Here is the Root of the service</h1>
    <a href='http://127.0.0.1:5000/home'>Home</a>
    '''
    return content # a STRING of content, which happens to be html

@app.route('/home')
def home():
    return '<h2>Welcome to the Flask Microservice Home</h2>'

@app.route('/data')
def data():
    struct = {'name':'Deidre', 'age':42, 'member':True}
    # all data must be ebcoded to be passed to the URI
    struct_j = json.dumps(struct)
    return struct_j

@app.route('/hello')
@app.route('/hello/<name>') # the angle-brackets indicate a parameter
def hello(name=''): # empty string evaluates to False
    # return 'hello anonymous user'
    # Flask will look in the templates folder when rendering a template
    return render_template('username.html', name=name)

@app.route('/kitten/<w>/<h>')
@app.route('/kiten/<w>/<h>') # we can capture common mispellings
@app.route('/tika/<w>/<h>')
def kitten(w='640', h='480'):
    return render_template('kitten.html', w=w, h=h)

@app.route('/osm')
@app.route('/osm/<lon>')
@app.route('/osm/<lon>/<lat>')
def osm(lon=-7.900, lat=53.429):
    return render_template('osm_map.html', lon=lon, lat=lat)

# last of all....
@app.errorhandler(404) # we can capture any code
def page_not_found(error):
    return render_template('page_not_found.html')

if __name__ == '__main__':
    app.run() # call the app into play (run the microservice as a server)
    # to exercise this code:
    # - run this module (creates a server)
    # - open a browser
    # browse to http://127.0.0.1:5000
