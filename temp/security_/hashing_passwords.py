import bcrypt


password = b"987456"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)
