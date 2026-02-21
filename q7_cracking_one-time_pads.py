c1 = "tviizuasex"
c2 = "uqdyjpbgix"

words = set()

with open("10-letter-words.txt") as f:
    for line in f:
        word = line.strip()
        
        if len(word) == 10:
            if word.isalpha():
                words.add(word)
                
D = []
for i in range(10):
    c1_val = ord(c1[i]) - ord('a')
    c2_val = ord(c2[i]) - ord('a')
    diff = (c1_val - c2_val) % 26
    D.append(diff)
                
for p1 in words:
    key = ""
    
    for i in range(10):
        c_val = ord(c1[i]) - ord('a')
        p_val = ord(p1[i]) - ord('a')
        
        k_val = (c_val - p_val) % 26
        
        key_letter = chr(k_val + ord('a'))
        key = key + key_letter
        
    p2 = ""
    
    for i in range(10):
        c_val = ord(c2[i]) - ord('a')
        k_val = ord(key[i]) - ord('a')
        
        p_val = (c_val - k_val) % 26
        
        plain_letter = chr(p_val + ord('a'))
        p2 = p2 + plain_letter
        
    if p2 in words:
        
        ok = True
        for i in range(10):
            p1_val = ord(p1[i]) - ord('a')
            p2_val = ord(p2[i]) - ord('a')
            diff_plain = (p1_val - p2_val) % 26
            
            if diff_plain != D[i]:
                ok = False
                break
            
        if ok:
            print("Plaintext 1: ", p1)
            print("Plaintext 2: ", p2)
            print("Key: ", key)
            break