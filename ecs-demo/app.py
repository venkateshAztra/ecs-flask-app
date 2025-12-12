from flask import Flask, request

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} {request.path} from {request.remote_addr}")

@app.route("/")
def hello():
    print("Handling / request")   # Optional
    return "Hello from ECS! v2222"

app.run(host="0.0.0.0", port=8080)
