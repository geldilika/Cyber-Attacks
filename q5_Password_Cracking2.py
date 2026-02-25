import hashlib
from itertools import product
import string

target_hash = "3c0f5ed09f04ad287d8c9a4868e1cc0846b8bc6e04790f4308d3b1d2e4d29d24"
salt = "yUVyqj7EeM9GdUgntmfikXHV"

names = [
    "Luna","Bella","Milo","Teddy","Daisy","Max","Poppy","Coco","Buddy","Rosie",
    "Lola","Bailey","Nala","Rex","Willow","Alfie","Molly","Archie","Ruby","Toby",
    "Charlie","Maisie","Bonnie","Hugo","Millie","Loki","Rocco","Frankie","Skye","Mabel",
    "Tilly","Bruno","Bear","Olive","Jasper","Winnie","Ziggy","Pepper","Beau","Maple",
    "Marley","George","Freddie","Suki","Belle","Cookie","Chester","Dolly","Honey","Indie"
]

sub = {
    "o": ["o", "0", "*"], "O": ["O", "0", "*"],
    "i": ["i", "1", "!"], "I": ["I", "1", "!"],
    "l": ["l", "1"],      "L": ["L", "1"],
    "a": ["a", "4", "@", "&"], "A": ["A", "4", "@", "&"],
    "e": ["e", "3"],      "E": ["E", "3"],
    "s": ["s", "$", "5"], "S": ["S", "$", "5"],
}

def variants(word):
    pools = [sub.get(ch, [ch]) for ch in word]
    for combo in product(*pools):
        yield "".join(combo)

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

checked = 0

for dog in names:
    # Try common case forms (this is what your code was missing)
    for base_word in {dog, dog.lower(), dog.upper()}:
        for base in variants(base_word):
            for d in range(100):
                pwd = base + f"{d:02d}"
                checked += 1

                # per spec: hash(password + salt)
                if sha256_hex(pwd + salt) == target_hash:
                    print("FOUND!")
                    print("Dog name:", dog)
                    print("Password:", pwd)
                    print("Checked:", checked)
                    raise SystemExit

print("No match found. Checked:", checked)