import datetime
import time
import jwt

secret = "shlyapa27"

payload = {
    "my_name": "Platon",
    "age": 27,
    "favorite_city": "Bern",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500),
}

encode_jwt = jwt.encode(payload=payload, key=secret, algorithm="HS256")
print(encode_jwt)


decoded = jwt.decode(
    encode_jwt,
    'shlyapa26',
    algorithms=["HS256"],
)

print(decoded)
