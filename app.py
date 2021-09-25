from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    "switeched to dev"
    return 'bye bye world'

if __name__ == '__main__':
    app.run()