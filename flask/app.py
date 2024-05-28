from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3 style="color:blue; text-align:center; margin:auto; margin-top:20vh;font-size:3em;">Welcome on my Web site :)</h3>'

app.run(host='0.0.0.0', port=81)