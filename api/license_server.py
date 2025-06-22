def handler(event, context):
    import urllib.parse

    VALID_LICENSES = {
        "LIVE-123456": "active",
        "LIVE-ABCDEF": "active",
        "TEST-000000": "expired"
    }

    # Parse query string parameters from event
    query = event.get("queryStringParameters") or {}
    key = query.get("key")

    if key in VALID_LICENSES and VALID_LICENSES[key] == "active":
        status = 200
        body = "valid"
    else:
        status = 403
        body = "invalid"

    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": body
    }
