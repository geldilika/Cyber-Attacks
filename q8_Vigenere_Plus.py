cipher = "lxgwoocojzowpvfvvbayokhycydlojplqaiygsomfbtyibaspnjlhxtytalqglusxpvtwaieuwwapsgxodfbqhfoljwlwubsgxopacucwywyfyqznofczloocewunxgmzvnrplcaieugcvvixchzleaqospyhcfonqzyblgbxbwubnjeomacfitpysyykapcumdaiouyyiveqhwubsxtoonerisvfxllohoacygugujloznlrovsnjiithyqjvodfaqhwtlwxvozleahiyfjiygpygjvqpgociflkqdmutnyuthhonpixwnyccqpkddviufshozkfbjthllbpqiskoltwubnplqlkfhvzslqxvsonbiitkfliybzpsgybzlujeouopvthlgcpctvojhnaltahnpfjoqniuldqcuiwoltqphnjkpkonxvauflpzuagerisynohzplmojdplgcriwkzoqogpynpluzvyqduyaeugyhxjiyctvsgzocnbdhbllxekpafdxbodpjimtsxjiotrljwlohdfhcfhyxhnyhxsambvonpiphvwiyzvdegtcffahlohjcuhoyuaqqblljvlozioyotjioaqospyrqhpyppotnplgxotfcavidocgxwudnpljlaqzotupltitkkckypfuegxoynyetoyocwygunjplthkgiybbsyuhwmpjzyblycghijobxvgskqzliubjjcgfhciibkkqfmblpluyokffripcljxmtaiyuiqxveclosfflmuyhoyyiwkouyokycgzohkihaqaldbotnjoqniukqjvoandqcfonkvivoqjpfonecewugszxouonpafyxjjtgsdipnp"

ALPH = "abcdefghijklmnopqrstuvwxyz"
A2I = {}
for i, ch in enumerate(ALPH):
    A2I[ch] = i

I2A = {}
for i, ch in enumerate(ALPH):
    I2A[i] = ch

def clean(s):
    s = s.lower()
    result = ""
    for ch in s:
        if ch in ALPH:
            result = result + ch
    return result

def split_columns(ct, l):
    cols = [""] * l
    for i, ch in enumerate(ct):
        col_index = i % l
        cols[col_index] = cols[col_index] + ch
    return cols

def reconstruct(cols_plain, l, total_len):
    out = []
    idxs = [0] * l
    for i in range(total_len):
        j = i % l
        out.append(cols_plain[j][idxs[j]])
        idxs[j] += 1
        
    return "".join(out)

COMMON_BIGRAMS = {
    "th","he","in","er","an","re","on","at","en","nd","ti","es","or","te","of","ed",
    "is","it","al","ar","st","to","nt","ng","se","ha","as","ou","io","le","ve"
}
COMMON_TRIGRAMS = {
    "the","and","ing","her","hat","his","tha","ere","for","ent","ion","ter","was","you","ith"
}
COMMON_CHUNKS = [
    "the","and","that","with","only","when","they","this","have","from","were",
    "said","think","people","need","always","here","well","one","their","mind",
]

def score_text(text):
    score = 0
    for i in range(len(text) - 1):
        if text[i:i+2] in COMMON_BIGRAMS:
            score += 2
    for i in range(len(text) - 2):
        if text[i:i+3] in COMMON_TRIGRAMS:
            score += 5
    for w in COMMON_CHUNKS:
        score += 20 * text.count(w)
    return score

def poly_base(a, b, c, p):
    return (a*(p**3) + b*(p**2) + c*p) % 26

def build_inv0_if_perm(a, b, c):
    inv0 = [-1] * 26
    for p in range(26):
        y = poly_base(a, b, c, p)
        if inv0[y] != -1:
            return None
        inv0[y] = p
    return inv0

def decrypt_column(col_ct, inv0, k):
    out = []
    for ch in col_ct:
        y = A2I[ch]
        p = inv0[(y - k) % 26]
        out.append(I2A[p])
    return "".join(out)

def keyword_from_chosen(chosen):
    keyword = ""
    for items in chosen:
        k = items[3]
        letter = I2A[k]
        keyword = keyword + letter
    return keyword

def triples_from_chosen(chosen):
    triples = []
    for items in chosen:
        a = items[0]
        b = items[1]
        c = items[2]
        triples.append([a,b,c])
    return triples

def crack_for_m(ct, m, valid_abc, keep_top=25):
    cols = split_columns(ct, m)
    top_per_col = []

    for j, col in enumerate(cols):
        cands = []
        for (a,b,c,inv0) in valid_abc:
            for k in range(26):
                pt_col = decrypt_column(col, inv0, k)
                sc = score_text(pt_col)
                cands.append((sc, (a,b,c,k), pt_col))
        cands.sort(key=lambda x: x[0], reverse=True)
        top_per_col.append(cands[:keep_top])

    choice = [0] * m

    def build_plain(choice):
        cols_plain = []
        for j in range(m):
            cols_plain.append(top_per_col[j][choice[j]][2])
        return reconstruct(cols_plain, m, len(ct))

    best_plain = build_plain(choice)
    best_score = score_text(best_plain)

    improved = True
    while improved:
        improved = False
        for j in range(m):
            cur = choice[j]
            for alt in range(keep_top):
                if alt == cur:
                    continue
                test_choice = choice[:]
                test_choice[j] = alt
                test_plain = build_plain(test_choice)
                test_score = score_text(test_plain)
                if test_score > best_score:
                    choice = test_choice
                    best_plain = test_plain
                    best_score = test_score
                    improved = True
                    break
            if improved:
                break

    chosen = []
    for j in range(m):
        candidate_index = choice[j]
        candidate_tuple = top_per_col[j][candidate_index]
        parameters = candidate_tuple[1]
        chosen.append(parameters)
    return best_score, best_plain, chosen

ct = clean(cipher)

print("cipher length:", len(ct))

valid_abc = []

for a in range(1, 26):          # a > 0
    for b in range(1, 26):      # b > 0
        for c in range(26):
            inv0 = build_inv0_if_perm(a, b, c)
            if inv0 is None:
                continue
            valid_abc.append((a, b, c, inv0))

print("valid (a,b,c) with a>0,b>0:", len(valid_abc))
print("-"*40)

M_MIN = 1
M_MAX = 20
KEEP_TOP = 25

best_overall = None

for m in range(M_MIN, M_MAX+1):
    sc, pt, chosen = crack_for_m(ct, m, valid_abc, keep_top=KEEP_TOP)
    print("m=", m, " score=", sc, " keyword=", keyword_from_chosen(chosen))
    if best_overall is None or sc > best_overall[0]:
        best_overall = (sc, m, pt, chosen)

print("="*60)
best_score, best_m, best_pt, best_chosen = best_overall

print("BEST SCORE:", best_score)
print("KEYLENGTH:", best_m)
print("KEYWORD:", keyword_from_chosen(best_chosen))
print("TRIPLES:", triples_from_chosen(best_chosen))
print("PLAINTEXT (no spaces/punct):")
print(best_pt)