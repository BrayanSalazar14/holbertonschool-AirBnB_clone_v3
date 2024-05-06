#!/usr/bin/python3
"""
Module that starts an API
"""


from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['/*', '0.0.0.0'])
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    storage.close()


def status_404(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.register_error_handler(404, status_404)
    app.debug = True
    app.run(host="0.0.0.0", port=5000, threaded=True)
