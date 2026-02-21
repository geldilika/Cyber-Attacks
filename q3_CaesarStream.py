cipher = "KpnwfdgjhncsypfdikirinjaflwalxrpabsxzkbnsqbfdrjlbsykvfdsamxotvmrximcykchfyajvgkbzhjuxjycrpartuTpevkituJvlbdmv"

def stream_decrypt(cipher, k, i):
    C = []
    for ch in cipher:
        if ch.isalpha():
            value = ord(ch.lower()) - ord('a')
            C.append(value)
            
    p = []
    p.append((C[0] - k - i) % 26)
    for j in range(1, len(C)):
        p.append((C[j] - k - C[j-1]) % 26)
        
    result = ""
    
    for x in p:
        letter = chr(x + ord('a'))
        result += letter
        
    return result

for k in range(26):
    for i in range(26):
        pt = stream_decrypt(cipher, k, i)
        
        print("k =", chr(k+97), "i =", chr(i+97))
        print(pt)
        print("-"*40)
