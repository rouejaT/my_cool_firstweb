from flask import Flask

app = Flask()
@app.route("/")

def index():
    return  " Hello world"
    


app.run(host='0.0.0.0', port=80, debug=True)