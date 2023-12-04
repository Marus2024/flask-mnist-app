from flask import Flask

app = Flask(__name__)
@app.route('/')#http://127.0.0.1:5000/ 以降のパスを指定する
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run()