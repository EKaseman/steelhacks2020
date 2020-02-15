from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html")




if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
