from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi I'm glad you're here"

@app.route('/status')
def status():
    d = {'status': True, 'time': datetime.now()}
    return d

if __name__ == "__main__":
    app.run()
