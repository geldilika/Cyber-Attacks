import hashlib

target_hash = "2b1025d47735fe8062ac97c53acf4c1e042554551a0af3a31024a745b66aa5c6"
salt = "yEyXEStiQPAd"

with open("ukenglish.txt", "r") as f:
    for line in f:
        word = line.strip()
        
        test = word + salt
        hash = hashlib.sha256(test.encode()).hexdigest()
        
        if hash == target_hash:
            print("Password found: ", word)