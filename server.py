"""
Launch REST server for WIDE DEMO
"""

import os
import sys
import xml.dom.minidom
import bottle
from bottle import response, request, static_file


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SRC_PATH = DIR_PATH + "/src"

app = bottle.app()



@app.get("/api/xml")
def test_xml():
    """For test just return pretty xml"""
    with open(DIR_PATH + "/src/test.xml") as f:
        xml_str = "".join(f.readlines())
    parsed_xml = xml.dom.minidom.parseString(xml_str)
    return parsed_xml.toprettyxml()


# Fot static files

@app.get("/")
def index():
    """Serve index.html""" 
    return static_file("index.html", root=SRC_PATH)

@app.get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root=SRC_PATH + "/js")

@app.get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root=SRC_PATH + "/css")

@app.get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root=SRC_PATH + "/img")

@app.get('/fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts1(filename):
    return static_file(filename, root=SRC_PATH + "/fonts")

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts2(filename):
    return static_file(filename, root=SRC_PATH + '/fonts')


app.run(host='0.0.0.0', port=8080)
