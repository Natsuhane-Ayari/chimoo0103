import hashlib

text = "測試"
sha512value = hashlib.sha512(text.encode('utf-8')).hexdigest()
print(sha512value)