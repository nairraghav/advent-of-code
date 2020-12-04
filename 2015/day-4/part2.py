import hashlib

hash_start = "iwrupvqb"
counter = 1

while True:
	result = hashlib.md5(f"{hash_start}{counter}".encode())
	if result.hexdigest()[:6] == "000000":
		print(counter)
		break
	counter += 1