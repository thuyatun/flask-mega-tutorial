from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! my name is thuyatun"

if __name__ == "__main":
    app.run(debug=True)
