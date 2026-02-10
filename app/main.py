from flask import Flask
from prometheus_client import start_http_server, Counter
import random
import time

app = Flask(__name__)

# יצירת מטריקה מותאמת אישית: סופר בקשות
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests to the app')

@app.route('/')
def home():
    REQUEST_COUNT.inc() # הגדלת המונה
    return "<h1>Monitoring V2!</h1><p>Refreshes are now counted in Prometheus.</p>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    # הפעלת שרת המטריקות בפורט 8000
    start_http_server(8000)
    # הפעלת האפליקציה בפורט 5000
    app.run(host='0.0.0.0', port=5000)