from flask import Flask, request

app = Flask(__name__)

VALID_LICENSES = {
    "LIVE-123456": "active",
    "LIVE-ABCDEF": "active",
    "TEST-000000": "expired"
}

@app.route("/api/validate")
def validate():
    key = request.args.get("key")
    if key in VALID_LICENSES and VALID_LICENSES[key] == "active":
        return "valid", 200
    else:
        return "invalid", 403

def handler(environ, start_response):
    return app(environ, start_response)
