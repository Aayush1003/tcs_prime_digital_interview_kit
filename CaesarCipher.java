/**
 * TCS NQT 2020 - Caesar Cipher Problem
 * Approach 1: Simple Character Iteration
 */

public class CaesarCipher {
    public static String customCaesarCipher(int key, String message) {
        if (key < 0) {
            return "INVALID INPUT";
        }
        
        StringBuilder encrypted = new StringBuilder();
        
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                char encrypted_char = (char) ((c - base + key) % 26 + base);
                encrypted.append(encrypted_char);
            } else if (Character.isDigit(c)) {
                int digit = Character.getNumericValue(c);
                int encrypted_digit = (digit + key) % 10;
                encrypted.append(encrypted_digit);
            } else {
                encrypted.append(c);  // Keep other characters as is
            }
        }
        
        return "The encrypted Text is: " + encrypted.toString();
    }
    
    public static void main(String[] args) {
        System.out.println("=== CAESAR CIPHER TEST ===");
        System.out.println("Input: key=1, message='All the Best'");
        System.out.println(customCaesarCipher(1, "All the Best"));
        
        System.out.println("\nInput: key=2, message='Hello 123'");
        System.out.println(customCaesarCipher(2, "Hello 123"));
        
        System.out.println("\nInput: key=25, message='ABC xyz 789'");
        System.out.println(customCaesarCipher(25, "ABC xyz 789"));
        
        System.out.println("\nInput: key=-1, message='Test'");
        System.out.println(customCaesarCipher(-1, "Test"));
        
        System.out.println("\nInput: key=5, message='Code-2023'");
        System.out.println(customCaesarCipher(5, "Code-2023"));
    }
}
