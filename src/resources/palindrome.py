from . import routes
from src.common import largest_palindrome, check_token
from src.extensions import drive_redis
# from flask import Flask, request, Blueprint
from flask import request


@routes.route('/api/history', methods=["GET"])
@check_token
def history_palindrome():
    ''' this function returns the last 10 palindrome values that were found within the api  '''
    try:
        values = drive_redis.get_db().keys('*')[:10]
    except Exception as e:
        print(e)
        return {"Message": "Not founding the history"}, 500

    response = {}
    if len(values) < 10:
        lenght = len(values) - 1
    else:
        lenght = 10

    for i in range(lenght):

        response[str(i)] = values[i].decode("utf-8")

    return response, 200


@routes.route('/api/palindromo', methods=["POST"])
@check_token
def get_palindrome_json():
    '''  main function where it receives as input a json, inside
    the payload it receives a parameter called palindrome, which
    will be the string to find the word palindrome in this, the
    endpoint will return the sub string with the word found and
    will save it in a database. '''
    json_data = request.json

    if not "palindromo" in json_data:
        return {'Message': "missing the palindrome value"}, 422

    largest_p = largest_palindrome(json_data['palindromo'])
    if not largest_p:
        return {"Message": "There is not palindrome word in the string"}, 400

    response = {
        "palindrome_word": json_data['palindromo'],
        "largest_palindrome_word": largest_p
    }
    # save to db
    key = 'palindrome word {} => {}'.format(json_data['palindromo'], largest_p)
    try:
        drive_redis.get_db().set(key, largest_p)
    except Exception as e:
        print(e)

    return response, 200
