#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

from calendar import timegm
from datetime import datetime
import _strptime  # https://bugs.python.org/issue7980
from flask import Flask, request, jsonify

APP = Flask(__name__)
APP.debug = True


def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())


@APP.route('/')
def health_check():
    return 'This datasource is healthy.'


@APP.route('/search', methods=['POST'])
def search():
    return jsonify(['avg_usage', 'avg_containers', 'complexQuery(abc.x)'])


@APP.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    dFrom = convert_to_time_ms(req['range']['from'])
    dTo = convert_to_time_ms(req['range']['to'])
    diff = (dTo - dFrom)/7
    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": [
                [861, dFrom],
                [753, dFrom + 1*diff],
                [652, dFrom + 2*diff],
                [766, dFrom + 3*diff],
                [865, dFrom + 4*diff],
                [733, dFrom + 5*diff],
                [622, dTo]
            ]
        }
    ]
    print (data)
    return jsonify(data)


@APP.route('/annotations', methods=['POST'])
def annotations():
    req = request.get_json()
    data = [
        {
            "annotation": 'This is the annotation 1',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 2,
            "title": 'Deployment notes 1',
            "tags": ['tag1', 'tag2'],
            "text": 'Hm, something went wrong...'
        },
        {
            "annotation": 'This is the annotation 2',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 4*2,
            "title": 'Deployment notes 2',
            "tags": ['tag1', 'tag2'],
            "text": 'All is fine. Maybe Maintenance.'
        }
    ]
    return jsonify(data)


@APP.route('/tag-keys', methods=['POST'])
def tag_keys():
    data = [
        {"type": "string", "text": "City"},
        {"type": "string", "text": "Country"}
    ]
    return jsonify(data)


@APP.route('/tag-values', methods=['POST'])
def tag_values():
    req = request.get_json()
    if req['key'] == 'City':
        return jsonify([
            {'text': 'Tokyo'},
            {'text': 'São Paulo'},
            {'text': 'Jakarta'}
        ])
    elif req['key'] == 'Country':
        return jsonify([
            {'text': 'China'},
            {'text': 'India'},
            {'text': 'United States'}
        ])



def run(Listen='0.0.0.0', Port=5000, Debug=False):
    if(not isinstance(Port, int)): raise Exception('Port has to be an integer')
    APP.run(host=Listen, port=Port, debug=Debug)