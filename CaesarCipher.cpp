/*
 * TCS NQT 2020 - Caesar Cipher Problem
 * Approach 1: Simple Character Iteration
 */

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string customCaesarCipher(int key, string message) {
    if (key < 0) {
        return "INVALID INPUT";
    }
    
    string encrypted = "";
    
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char encrypted_char = (char)((c - base + key) % 26 + base);
            encrypted += encrypted_char;
        } else if (isdigit(c)) {
            int digit = c - '0';
            int encrypted_digit = (digit + key) % 10;
            encrypted += (char)('0' + encrypted_digit);
        } else {
            encrypted += c;
        }
    }
    
    return "The encrypted Text is: " + encrypted;
}

int main() {
    cout << "=== CAESAR CIPHER TEST ===" << endl;
    
    cout << "Input: key=1, message='All the Best'" << endl;
    cout << customCaesarCipher(1, "All the Best") << endl;
    
    cout << "\nInput: key=2, message='Hello 123'" << endl;
    cout << customCaesarCipher(2, "Hello 123") << endl;
    
    cout << "\nInput: key=25, message='ABC xyz 789'" << endl;
    cout << customCaesarCipher(25, "ABC xyz 789") << endl;
    
    cout << "\nInput: key=-1, message='Test'" << endl;
    cout << customCaesarCipher(-1, "Test") << endl;
    
    cout << "\nInput: key=5, message='Code-2023'" << endl;
    cout << customCaesarCipher(5, "Code-2023") << endl;
    
    return 0;
}
