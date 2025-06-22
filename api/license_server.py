# api/license_server.py

def handler(event, context):
    VALID_LICENSES = {
        "LIVE-123456": "active",
        "LIVE-ABCDEF": "active",
        "TEST-000000": "expired"
    }

    key = None

    if "queryStringParameters" in event and event["queryStringParameters"]:
        key = event["queryStringParameters"].get("key")

    if key in VALID_LICENSES and VALID_LICENSES[key] == "active":
        return {
            "statusCode": 200,
            "body": "valid"
        }
    else:
        return {
            "statusCode": 403,
            "body": "invalid"
        }
