import hashlib


def sha256_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()



my_string = "58aaa4bfa6a1010062b701ed60c3a6ac"
hashed_string = sha256_hash(my_string)
print(hashed_string)