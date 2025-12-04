from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)