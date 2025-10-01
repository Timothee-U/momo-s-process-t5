import base64

#Credentials
USERNAME = "team5"
PASSWORD = "team!123=5"

def check_auth(header):
    if not header or not header.startswith("Basic "):
        return False
    encoded = header.split(" ")[1]
    decoded = base64.b64decode(encoded).decode()
    user, pw = decoded.split(":")
    return user == USERNAME and pw == PASSWORD