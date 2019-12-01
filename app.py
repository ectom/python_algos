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
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    num = args['num']
    arr = [num] + arr
    return {'arr': arr}, 200


@app.route('/insertAt', methods=['POST'])
def insert_at():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    num = args['num']
    idx = args['idx']
    arr = arr[:idx] + [num] + arr[idx:]
    return {'arr': arr}, 200


@app.route('/popFront', methods=['GET'])
def pop_front():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    arr = arr[1:]
    return {'arr': arr}, 200


@app.route('/removeAt', methods=['GET'])
def remove_at():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    idx = args['idx']
    arr = arr[:idx] + arr[idx + 1:]
    return {'arr': arr}, 200


@app.route('/swapPairs', methods=['GET'])
def swap_pairs():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    if len(arr) % 2 == 0:
        even = len(arr)
    else:
        even = len(arr) - 1
    i = 0
    while i < even:
        print(i)
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
        i = i + 2
    return {'arr': arr}, 200


@app.route('/removeDuplicates', methods=['GET'])
def remove_duplicates():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    temp = arr[0]
    i = 1
    while i < len(arr):
        if temp == arr[i]:
            arr = arr[:i] + arr[i + 1:]
        else:
            temp = arr[i]
            i = i + 1
    return {'arr': arr}, 200


@app.route('/minToFront', methods=['GET'])
def min_to_front():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    min = arr[0]
    mindex = 0
    for idx, i in enumerate(arr):
        if min > i:
            min = i
            mindex = idx
    arr = [min] + arr[:mindex] + arr[mindex + 1:]
    return {'arr': arr}, 200


@app.route('/reverseArray', methods=['GET'])
def reverse_array():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[-(i + 1)]
        arr[-(i + 1)] = temp
    return {'arr': arr}, 200


@app.route('/rotate', methods=['POST'])
def rotate():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('shift_by', type='int', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    shift_by = parser.parse_args()['shift_by']
    for i in range(shift_by):
        k = len(arr) - 1
        temp = arr[k]
        k = k - 1
        while k >= 0:
            arr[k + 1] = arr[k]
            k = k - 1
        arr[0] = temp
    return {'arr': arr}, 200


@app.route('/filterRange', methods=['POST'])
def filter_range():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('mini', type='int', required='true')
    parser.add_argument('maxi', type='int', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    mini = parser.parse_args()['mini']
    maxi = parser.parse_args()['maxi']
    for i, val in enumerate(arr):
        if mini < val < maxi:
            arr = arr[:i] + arr[i + 1:]
    return {'arr': arr}, 200


@app.route('/arrConcat', methods=['POST'])
def arr_concat():
    parser = reqparse.RequestParser()
    parser.add_argument('arr1', action='append', required='true')
    parser.add_argument('arr2', action='append', required='true')
    arr1 = ast.literal_eval(parser.parse_args()['arr1'][0])
    arr2 = ast.literal_eval(parser.parse_args()['arr2'][0])
    return {'arr': arr1 + arr2}, 200


@app.route('/skyline', methods=['GET'])
def skyline():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    new_arr = []
    curr = 0
    for val in arr:
        if curr < val:
            new_arr.append(val)
            curr = val
    return {'arr': new_arr}, 200


@app.route('/removeNegatives', methods=['GET'])
def remove_negatives():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr = arr[:i] + arr[i+1:]
            i = i - 1
        i = i + 1
    return {'arr': arr}, 200


@app.route('/secondToLast', methods=['GET'])
def second_to_last():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    if len(arr) >= 2:
        return {'second_to_last': arr[-2]}, 200

    return 502


@app.route('/nthToLast', methods=['GET'])
def nth_to_last():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('n', type='int', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'])
    n = parser.parse_args()['n']
    if len(arr) >= n:
        print(arr[-n])
        return {'nth_to_last': arr[-n]}, 200
    return 502


@app.route('/secondLargest', methods=['GET'])
def second_largest():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    print(arr)
    if len(arr) < 2:
        return {'message': 'Array is too short'}, 502
    if arr[0] > arr[1]:
        largest = arr[0]
        second = arr[1]
    largest = arr[1]
    second = arr[0]
    for i in range(2, len(arr)):
        if second < arr[i] < largest:
            second = arr[i]
        elif arr[i] > largest:
            second = largest
            largest = arr[i]
    return {'second': second}, 200


if __name__ == '__main__':
    app.run()
