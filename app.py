from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", server_time=server_time)

@app.route('/health')
def health():
    return jsonify(status="ok", message="Service is healthy")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
