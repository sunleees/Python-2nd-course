import hashlib

data = "hello".encode()
print(data)

hash_value = hashlib.sha256(data).hexdigest()
print(hash_value)
