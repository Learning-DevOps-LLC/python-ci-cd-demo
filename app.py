from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from CI/CD Pipeline!<br>Ashish Singh"

@app.route('/health')
def health():
    return {"status": "ok", "message": "Service is healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
