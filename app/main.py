from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"

def isDiff(first,second):
    sames = 0
    num = 0
    flag = true
    for each in first:
        num = num + 1
        for each2 in second:
            if (first["ingredients"][each] == second["ingredients"][each2]):
                sames = sames + 1
    if (sames == len(second)):
        sames = sames - 1
    sames = sames / len(first)
    if (sames > 70):
        flag = true
    else:
        flag = false
    return flag


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
