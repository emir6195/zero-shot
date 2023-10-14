from flask import Flask, jsonify
from routes.zero_shot import router as zero_shot_router
from config import ins_config


host = ins_config.getDefault("host", "0.0.0.0")
port = ins_config.getDefault("port", "5061")

app = Flask(__name__)
app.register_blueprint(zero_shot_router, url_prefix="/zero-shot")


@app.errorhandler(500)
def api_error(e):
    return jsonify(code=500, error=str(e)), 500


if __name__ == "__main__":
    app.run(host, port, True)
