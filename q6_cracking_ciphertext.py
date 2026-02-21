cipher = "mufexbxhqwa"
partial_key = "j?np??zh?lw"

def to_num(c):
    return ord(c) - ord('a')

def to_chr(n):
    return chr(n % 26 + ord('a'))

with open("11-letter-words.txt") as f:
    for line in f:
        word = line.strip()
        
        if len(word) != 11:
            continue
        
        possible = True
        full_key = ""
        
        for i in range(11):
            k = (to_num(cipher[i]) - to_num(word[i])) % 26
            k_char = to_chr(k)
            full_key += k_char
            
            if partial_key[i] != "?" and partial_key[i] != k_char:
                possible = False
                break
            
        if possible:
            print("Plaintext: ", word)
            print("Full key: ", full_key)
            break