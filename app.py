from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Cloud!</h1><p>Deployed on Render</p>"

@app.route('/Status')
def Status():
    return {
        "Status": "running",
        "server": "Render"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)