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

def looks_english(s):
    t = s.lower()

    common = [" the ", " and ", " to ", " of ", " in ", " is "]
    count = 0
    for w in common:
        if w in t:
            count += 1
    if count < 2:
        return False

    letters = ""
    for ch in t:
        if ch.isalpha():
            letters += ch
    if len(letters) == 0:
        return False

    vowels = 0
    for ch in letters:
        if ch in "aeiou":
            vowels += 1
    ratio = vowels / len(letters)
    if ratio < 0.30 or ratio > 0.55:
        return False

    return True

found_any = False

for a in range(1, 26):
    for b in range(1, 26):
        for c in range(26):
            for k in range(26):

                inv = build_inverse(a, b, c, k)
                if inv is None:
                    continue

                text = decrypt(cipher, inv)

                if looks_english(text):
                    found_any = True
                    print("triple =", [a, b, c], "k =", chr(k + 97))
                    print(text)
                    print("-" * 40)

if not found_any:
    print("No results passed the simple English filter.")