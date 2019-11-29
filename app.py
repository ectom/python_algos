from flask import Flask
from flask_restful import Api, Resource, reqparse
import ast
import random

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/pushFront', methods=['POST'])
def push_front():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    num = args['num']
    lst = [num] + lst
    return {'list': lst}, 200

@app.route('/insertAt', methods=['POST'])
def insert_at():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    num = args['num']
    idx = args['idx']
    lst = lst[:idx] + [num] + lst[idx:]
    return {'list': lst}, 200

@app.route('/popFront', methods=['GET'])
def pop_front():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    lst = lst[1:]
    return {'list': lst}, 200

@app.route('/removeAt', methods=['GET'])
def remove_at():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    idx = args['idx']
    lst = lst[:idx] + lst[idx + 1:]
    return {'list': lst}, 200

@app.route('/swapPairs', methods=['GET'])
def swap_pairs():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    if len(lst) % 2 == 0:
        even = len(lst)
    else:
        even = len(lst) - 1
    i = 0
    while i < even:
        print(i)
        temp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = temp
        i = i + 2
    return {'list': lst}, 200

@app.route('/removeDuplicates', methods=['GET'])
def remove_duplicates():
    parser = reqparse.RequestParser()
    parser.add_argument('list', action='append', required='true')
    args = parser.parse_args()
    lst = ast.literal_eval(args['list'][0])
    temp = lst[0]
    i = 1
    while i < len(lst):
        if temp == lst[i]:
            lst = lst[:i] + lst[i + 1:]
        else:
            temp = lst[i]
            i = i + 1
    return {'list': lst}, 200


if __name__ == '__main__':
    app.run()
