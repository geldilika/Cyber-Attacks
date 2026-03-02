import hashlib
from itertools import product

target_hash = "fa533f66a3023914f16291b7ae8e975fabaa9a7344f85d66408db791cae9d3dd"
salt = "17U5atUk29ZQtUvLlR11Xvwc"

names = [
    "Luna","Bella","Milo","Teddy","Daisy","Max","Poppy","Coco","Buddy","Rosie",
    "Lola","Bailey","Nala","Rex","Willow","Alfie","Molly","Archie","Ruby","Toby",
    "Charlie","Maisie","Bonnie","Hugo","Millie","Loki","Rocco","Frankie","Skye","Mabel",
    "Tilly","Bruno","Bear","Olive","Jasper","Winnie","Ziggy","Pepper","Beau","Maple",
    "Marley","George","Freddie","Suki","Belle","Cookie","Chester","Dolly","Honey","Indie"
]

sub = {
    "o": ["o", "0", "*"], 
    "O": ["O", "0", "*"],
    "i": ["i", "1", "!"],
    "I": ["I", "1", "!"],
    "l": ["l", "1"],
    "L": ["L", "1"],
    "a": ["a", "4", "@", "&"],
    "A": ["A", "4", "@", "&"],
    "e": ["e", "3"],
    "E": ["E", "3"],
    "s": ["s", "$", "5"],
    "S": ["S", "$", "5"],
}

def variants(word):
    choices = []
    for ch in word:
        choices.append(sub.get(ch, [ch]))
    for combo in product(*choices):
        yield "".join(combo)

def sha256_hex(x):
    return hashlib.sha256(x.encode("utf-8")).hexdigest()

for dog in names:
    for base_word in {dog, dog.lower(), dog.upper()}:
        for base in variants(base_word):
            for d in range(100):
                pwd = base + str(d).zfill(2)
                if sha256_hex(pwd + salt) == target_hash:
                    print("FOUND!")
                    print("Password:", pwd)
                    print("Dog name:", dog)
                    raise SystemExit

print("No match found.")