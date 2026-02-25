# 🔐 COM2041 Cryptography Coursework (Python)

A collection of cryptanalysis and cipher-breaking tools built in **Python 3**.

This project focuses on attacking classical encryption schemes and salted password hashes using brute force, modular arithmetic, and statistical scoring.

---

## Features

### Classical Cipher Cracking
- Caesar cipher brute-force (all 26 shifts)
- CaesarPlus (polynomial Caesar) permutation validation
- CaesarStream key and initialization recovery
- English scoring via word and frequency detection

### Hash Cracking
- Salted **SHA-256** dictionary attack
- Wordlist-based password recovery
- Efficient hashing using Python `hashlib`

### Leetspeak Password Attack
- Rule-based substitutions:
  - `o → 0 / *`
  - `i → 1 / !`
  - `a → 4 / @ / &`
  - `e → 3`
  - `s → $ / 5`
  - `l → 1`
- Automatic two-digit suffix generation (`00–99`)
- Full salted hash verification

### Vigenère-Based Attacks
- Standard Vigenère decryption
- Partial key reconstruction
- Reused one-time pad exploit
- VigenerePlus (polynomial Vigenère variant)

---

## Methods Used
- **Brute-force search**
- **Dictionary attacks**
- **Frequency analysis**
- **Wordlist filtering**
- **Statistical language scoring**
- Modular arithmetic over ℤ₍₂₆₎
- Python standard library only

---

## Repository Structure
 - q1_caesar.py
 - q2_caesarplus.py
 - q3_caesarstream.py
 - q4_sha256_dictionary.py
 - q5_leetspeak_password.py
 - q6_vigenere_partial_key.py
 - q7_reused_onetimepad.py
 - q8_vigenereplus.py
 - ukenglish.txt
 - 10-letter-words.txt
 - 11-letter-words.txt
 - README.md


---

## How to Run

- python q1_caesar.py
