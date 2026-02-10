from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>K8s Cluster Monitoring Project</h1><p>I am a workload running on your cluster!</p>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)