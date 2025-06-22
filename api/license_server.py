def handler(request):
    VALID_LICENSES = {
        "LIVE-123456": "active",
        "LIVE-ABCDEF": "active",
        "TEST-000000": "expired"
    }

    key = request.args.get("key")
    if key in VALID_LICENSES and VALID_LICENSES[key] == "active":
        return ("valid", 200)
    else:
        return ("invalid", 403)
