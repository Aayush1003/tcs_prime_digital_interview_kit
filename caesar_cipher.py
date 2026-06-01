"""
TCS NQT 2020 - Caesar Cipher Problem
Multiple Approaches
"""

# ============================================
# APPROACH 1: Simple Character Iteration
# ============================================
def custom_caesar_cipher_v1(key, message):
    """Simple iteration approach"""
    if key < 0:
        return "INVALID INPUT"
    
    encrypted = ""
    
    for c in message:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            encrypted_char = chr((ord(c) - base + key) % 26 + base)
            encrypted += encrypted_char
        elif c.isdigit():
            digit = int(c)
            encrypted_digit = (digit + key) % 10
            encrypted += str(encrypted_digit)
        else:
            encrypted += c
    
    return f"The encrypted Text is: {encrypted}"


# ============================================
# APPROACH 2: Using Helper Functions
# ============================================
def encrypt_char(c, key):
    """Helper function to encrypt a single character"""
    base = ord('A') if c.isupper() else ord('a')
    return chr((ord(c) - base + key) % 26 + base)

def encrypt_digit(c, key):
    """Helper function to encrypt a digit"""
    digit = int(c)
    return str((digit + key) % 10)

def custom_caesar_cipher_v2(key, message):
    """Using helper functions for organization"""
    if key < 0:
        return "INVALID INPUT"
    
    encrypted = ""
    
    for c in message:
        if c.isalpha():
            encrypted += encrypt_char(c, key)
        elif c.isdigit():
            encrypted += encrypt_digit(c, key)
        else:
            encrypted += c
    
    return f"The encrypted Text is: {encrypted}"


# ============================================
# APPROACH 3: Using Lambda and Map
# ============================================
def custom_caesar_cipher_v3(key, message):
    """Using lambda functions and map"""
    if key < 0:
        return "INVALID INPUT"
    
    def process_char(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + key) % 26 + base)
        elif c.isdigit():
            return str((int(c) + key) % 10)
        return c
    
    encrypted = ''.join(map(process_char, message))
    return f"The encrypted Text is: {encrypted}"


# ============================================
# APPROACH 4: Using List Comprehension
# ============================================
def custom_caesar_cipher_v4(key, message):
    """Using list comprehension for conciseness"""
    if key < 0:
        return "INVALID INPUT"
    
    def encrypt(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + key) % 26 + base)
        elif c.isdigit():
            return str((int(c) + key) % 10)
        return c
    
    encrypted = ''.join([encrypt(c) for c in message])
    return f"The encrypted Text is: {encrypted}"


# ============================================
# APPROACH 5: One-Liner Version (Advanced)
# ============================================
def custom_caesar_cipher_v5(key, message):
    """One-liner version (not recommended for readability)"""
    if key < 0:
        return "INVALID INPUT"
    return "The encrypted Text is: " + ''.join(
        chr((ord(c) - (ord('A') if c.isupper() else ord('a')) + key) % 26 + (ord('A') if c.isupper() else ord('a'))) if c.isalpha() else
        str((int(c) + key) % 10) if c.isdigit() else
        c for c in message
    )


# ============================================
# APPROACH 6: Using Functional Programming
# ============================================
from functools import reduce

def custom_caesar_cipher_v6(key, message):
    """Using reduce for functional style"""
    if key < 0:
        return "INVALID INPUT"
    
    def process_char(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + key) % 26 + base)
        elif c.isdigit():
            return str((int(c) + key) % 10)
        return c
    
    encrypted = reduce(lambda acc, c: acc + process_char(c), message, "")
    return f"The encrypted Text is: {encrypted}"


# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    test_cases = [
        (1, "All the Best"),
        (2, "Hello 123"),
        (25, "ABC xyz 789"),
        (-1, "Test"),
        (5, "Code-2023"),
    ]
    
    print("=" * 70)
    print("CAESAR CIPHER - ALL APPROACHES")
    print("=" * 70)
    
    for key, message in test_cases:
        print(f"\nInput: key={key}, message='{message}'")
        print(f"  Approach 1: {custom_caesar_cipher_v1(key, message)}")
        print(f"  Approach 2: {custom_caesar_cipher_v2(key, message)}")
        print(f"  Approach 3: {custom_caesar_cipher_v3(key, message)}")
        print(f"  Approach 4: {custom_caesar_cipher_v4(key, message)}")
        print(f"  Approach 5: {custom_caesar_cipher_v5(key, message)}")
        print(f"  Approach 6: {custom_caesar_cipher_v6(key, message)}")
