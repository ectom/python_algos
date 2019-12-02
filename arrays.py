import time

from flask import Flask
from flask_restful import Api, Resource, reqparse
import ast

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def hello_world():
    start_time = time.time()
    return {'Hello World!': time.time() - start_time}, 200


@app.route('/pushFront', methods=['POST'])
def push_front():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    num = args['num']
    arr = [num] + arr
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/insertAt', methods=['POST'])
def insert_at():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('num', type=int, required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    num = args['num']
    idx = args['idx']
    arr = arr[:idx] + [num] + arr[idx:]
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/popFront', methods=['GET'])
def pop_front():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    arr = arr[1:]
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/removeAt', methods=['GET'])
def remove_at():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('idx', type=int, required='true')
    args = parser.parse_args()
    arr = ast.literal_eval(args['arr'][0])
    idx = args['idx']
    arr = arr[:idx] + arr[idx + 1:]
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/swapPairs', methods=['GET'])
def swap_pairs():
    start_time = time.time()
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
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/removeDuplicates', methods=['GET'])
def remove_duplicates():
    start_time = time.time()
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
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/minToFront', methods=['GET'])
def min_to_front():
    start_time = time.time()
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
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/reverseArray', methods=['GET'])
def reverse_array():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[-(i + 1)]
        arr[-(i + 1)] = temp
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/rotate', methods=['POST'])
def rotate():
    start_time = time.time()
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
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/filterRange', methods=['POST'])
def filter_range():
    start_time = time.time()
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
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/arrConcat', methods=['POST'])
def arr_concat():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr1', action='append', required='true')
    parser.add_argument('arr2', action='append', required='true')
    arr1 = ast.literal_eval(parser.parse_args()['arr1'][0])
    arr2 = ast.literal_eval(parser.parse_args()['arr2'][0])
    return {'arr': arr1 + arr2, 'time': time.time() - start_time}, 200


@app.route('/skyline', methods=['GET'])
def skyline():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    new_arr = []
    curr = 0
    for val in arr:
        if curr < val:
            new_arr.append(val)
            curr = val
    return {'arr': new_arr, 'time': time.time() - start_time}, 200


@app.route('/removeNegatives', methods=['GET'])
def remove_negatives():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr = arr[:i] + arr[i + 1:]
            i = i - 1
        i = i + 1
    return {'arr': arr, 'time': time.time() - start_time}, 200


@app.route('/secondToLast', methods=['GET'])
def second_to_last():
    start_time = time.time()
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    if len(arr) >= 2:
        return {'second_to_last': arr[-2], 'time': time.time() - start_time}, 200
    return {'message': 'array too short', 'time': time.time() - start_time}, 502


@app.route('/nthToLast', methods=['GET'])
def nth_to_last():
    parser = reqparse.RequestParser()
    parser.add_argument('arr', action='append', required='true')
    parser.add_argument('n', type='int', required='true')
    arr = ast.literal_eval(parser.parse_args()['arr'][0])
    n = parser.parse_args()['n']
    if len(arr) >= n:
        return {'nth_to_last': arr[-n]}, 200
    return {'message': 'array too short'}, 502


def second_largest(arr):
    if len(arr) < 2:
        return 'Array is too short'
    if arr[0] > arr[1]:
        largest = arr[0]
        second = arr[1]
    else:
        largest = arr[1]
        second = arr[0]
    for i in range(2, len(arr)):
        if second < arr[i] < largest:
            second = arr[i]
        elif arr[i] > largest:
            second = largest
            largest = arr[i]
    return second


def nth_largest(arr, n):
    merge_sort(arr)
    return arr[-n]


def nth_smallest(arr, n):
    merge_sort(arr)
    return arr[n - 1]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def credit_card_validation(arr):
    last = arr.pop()
    i = 1
    while i <= len(arr):
        arr[-i] *= 2
        if arr[-i] > 9:
            arr[-i] -= 9
        i += 2
    everything = 0
    for val in arr:
        everything += val
    everything += last
    if everything % 10 == 0:
        return True
    return False


print(credit_card_validation([5, 2, 2, 8, 2]))
array = [2, 7, 6, 3, 9, 23, 7, 4, 0, 3]
print('Second Largest of [2,7,6,3,9,23,7,4,0,3] is ', second_largest(array))
print('Nth largest: ', nth_largest(array, 4))
print('Nth smallest: ', nth_smallest(array, 4))
array = [2, 7, 6, 3, 9, 23, 7, 4, 0, 3]
print('Merge Sort - Unsorted array: %s' % array)
merge_sort(array)
print('Calling Merge Sort: %s' % array)

if __name__ == '__main__':
    app.run()
