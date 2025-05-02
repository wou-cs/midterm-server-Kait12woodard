from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<n>", methods=["GET"])
def subtract_by_one(n):
    try:
        num = int(n)
    except ValueError:
        return '', 400
    if num < 1:
        return '', 404
    answer = {}
    result = num - 1
    answer['dec'] = result
    result = hex(num)
    answer['hex'] = result
    return answer
