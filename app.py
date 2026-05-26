from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Main page"
@app.route("/example")
def example():
    k = 10
    return f"Hi,Example {k}"

if __name__ == "__main__":
    app.run()
