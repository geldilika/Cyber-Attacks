cipher = "C ymdergwr icp gy iwxeyf gp zgy ydeeqz jmf ehqeexy gp zgy cqfgwpy. - Qwplmqgmy"

def build_inverse(a, b, c, k):
    inv = [-1]*26
    for p in range(26):
        ct = (a*(p**3) + b*(p**2) + c*p + k) % 26
        if inv[ct] != -1:
            return None
        inv[ct] = p
    return inv

def decrypt(text, inv):
    result = ""
    for ch in text:
        if ch.isalpha():
            v = ord(ch.lower()) - ord('a')
            p = inv[v]
            letter = chr(p + ord('a'))
            result += letter.upper() if ch.isupper() else letter
        else:
            result += ch
    return result

for a in range(1, 26):
    for b in range(1, 26):
        for c in range(26):
            for k in range(26):
                inv = build_inverse(a, b, c, k)
                if inv is None:
                    continue

                text = decrypt(cipher, inv)

                print([a,b,c], chr(k+97))
                print(text)
                print("-"*40)