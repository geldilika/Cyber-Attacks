def rot(c, shift):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c


def caesar(text, shift):
    return ''.join(rot(c, shift) for c in text)

cipher = "Fpvrapr fnaf pbafpvrapr a'rfg dhr ehvar qr y'nzr."
for shift in range(26):
    print(shift, caesar(cipher, shift))