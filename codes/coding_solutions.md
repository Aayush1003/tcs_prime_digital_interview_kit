# TCS NQT 2020 Coding Solutions

## Problem 1: WASHING MACHINE

### Approach 1: Simple If-Else Logic

#### Java
```java
public class WashingMachine {
    public static String getTimeEstimate(int weight) {
        if (weight < 0) {
            return "INVALID INPUT";
        }
        
        if (weight == 0) {
            return "Time Estimated: 0 Minutes";
        }
        
        if (weight > 7000) {
            return "OVERLOADED!";
        }
        
        if (weight <= 2000) {
            return "Time Estimated: 25 Minutes";
        } else if (weight <= 4000) {
            return "Time Estimated: 35 Minutes";
        } else {
            return "Time Estimated: 45 Minutes";
        }
    }
    
    public static void main(String[] args) {
        // Test cases
        System.out.println(getTimeEstimate(2000));    // 25 Minutes
        System.out.println(getTimeEstimate(3500));    // 35 Minutes
        System.out.println(getTimeEstimate(5000));    // 45 Minutes
        System.out.println(getTimeEstimate(8000));    // OVERLOADED!
        System.out.println(getTimeEstimate(0));       // 0 Minutes
        System.out.println(getTimeEstimate(-100));    // INVALID INPUT
    }
}
```

#### C++
```cpp
#include <iostream>
#include <string>
using namespace std;

string getTimeEstimate(int weight) {
    if (weight < 0) {
        return "INVALID INPUT";
    }
    
    if (weight == 0) {
        return "Time Estimated: 0 Minutes";
    }
    
    if (weight > 7000) {
        return "OVERLOADED!";
    }
    
    if (weight <= 2000) {
        return "Time Estimated: 25 Minutes";
    } else if (weight <= 4000) {
        return "Time Estimated: 35 Minutes";
    } else {
        return "Time Estimated: 45 Minutes";
    }
}

int main() {
    cout << getTimeEstimate(2000) << endl;    // 25 Minutes
    cout << getTimeEstimate(3500) << endl;    // 35 Minutes
    cout << getTimeEstimate(5000) << endl;    // 45 Minutes
    cout << getTimeEstimate(8000) << endl;    // OVERLOADED!
    cout << getTimeEstimate(0) << endl;       // 0 Minutes
    cout << getTimeEstimate(-100) << endl;    // INVALID INPUT
    return 0;
}
```

#### Python
```python
def get_time_estimate(weight):
    if weight < 0:
        return "INVALID INPUT"
    
    if weight == 0:
        return "Time Estimated: 0 Minutes"
    
    if weight > 7000:
        return "OVERLOADED!"
    
    if weight <= 2000:
        return "Time Estimated: 25 Minutes"
    elif weight <= 4000:
        return "Time Estimated: 35 Minutes"
    else:
        return "Time Estimated: 45 Minutes"

# Test cases
if __name__ == "__main__":
    print(get_time_estimate(2000))    # 25 Minutes
    print(get_time_estimate(3500))    # 35 Minutes
    print(get_time_estimate(5000))    # 45 Minutes
    print(get_time_estimate(8000))    # OVERLOADED!
    print(get_time_estimate(0))       # 0 Minutes
    print(get_time_estimate(-100))    # INVALID INPUT
```

---

### Approach 2: Using Dictionary/Map (Cleaner)

#### Java
```java
import java.util.*;

public class WashingMachineMap {
    static class Range {
        int min, max, time;
        Range(int min, int max, int time) {
            this.min = min;
            this.max = max;
            this.time = time;
        }
    }
    
    public static String getTimeEstimate(int weight) {
        if (weight < 0) {
            return "INVALID INPUT";
        }
        
        if (weight == 0) {
            return "Time Estimated: 0 Minutes";
        }
        
        if (weight > 7000) {
            return "OVERLOADED!";
        }
        
        List<Range> ranges = Arrays.asList(
            new Range(1, 2000, 25),
            new Range(2001, 4000, 35),
            new Range(4001, 7000, 45)
        );
        
        for (Range r : ranges) {
            if (weight >= r.min && weight <= r.max) {
                return "Time Estimated: " + r.time + " Minutes";
            }
        }
        
        return "INVALID INPUT";
    }
    
    public static void main(String[] args) {
        System.out.println(getTimeEstimate(2000));
        System.out.println(getTimeEstimate(3500));
        System.out.println(getTimeEstimate(5000));
    }
}
```

#### C++
```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Range {
    int min, max, time;
};

string getTimeEstimate(int weight) {
    if (weight < 0) return "INVALID INPUT";
    if (weight == 0) return "Time Estimated: 0 Minutes";
    if (weight > 7000) return "OVERLOADED!";
    
    vector<Range> ranges = {
        {1, 2000, 25},
        {2001, 4000, 35},
        {4001, 7000, 45}
    };
    
    for (auto& r : ranges) {
        if (weight >= r.min && weight <= r.max) {
            return "Time Estimated: " + to_string(r.time) + " Minutes";
        }
    }
    
    return "INVALID INPUT";
}

int main() {
    cout << getTimeEstimate(2000) << endl;
    cout << getTimeEstimate(3500) << endl;
    cout << getTimeEstimate(5000) << endl;
    return 0;
}
```

#### Python
```python
def get_time_estimate(weight):
    if weight < 0:
        return "INVALID INPUT"
    
    if weight == 0:
        return "Time Estimated: 0 Minutes"
    
    if weight > 7000:
        return "OVERLOADED!"
    
    ranges = [
        (1, 2000, 25),
        (2001, 4000, 35),
        (4001, 7000, 45)
    ]
    
    for min_w, max_w, time in ranges:
        if min_w <= weight <= max_w:
            return f"Time Estimated: {time} Minutes"
    
    return "INVALID INPUT"

# Test
if __name__ == "__main__":
    print(get_time_estimate(2000))
    print(get_time_estimate(3500))
    print(get_time_estimate(5000))
```

---

### Approach 3: Using Ternary Operator (Functional Style)

#### Java
```java
public class WashingMachineTernary {
    public static String getTimeEstimate(int weight) {
        return (weight < 0) ? "INVALID INPUT" :
               (weight == 0) ? "Time Estimated: 0 Minutes" :
               (weight > 7000) ? "OVERLOADED!" :
               (weight <= 2000) ? "Time Estimated: 25 Minutes" :
               (weight <= 4000) ? "Time Estimated: 35 Minutes" :
               "Time Estimated: 45 Minutes";
    }
    
    public static void main(String[] args) {
        System.out.println(getTimeEstimate(2000));
    }
}
```

#### Python
```python
def get_time_estimate(weight):
    return ("INVALID INPUT" if weight < 0 else
            "Time Estimated: 0 Minutes" if weight == 0 else
            "OVERLOADED!" if weight > 7000 else
            "Time Estimated: 25 Minutes" if weight <= 2000 else
            "Time Estimated: 35 Minutes" if weight <= 4000 else
            "Time Estimated: 45 Minutes")

print(get_time_estimate(2000))
```

---

## Problem 2: CAESAR CIPHER

### Approach 1: Simple Character Iteration

#### Java
```java
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
        System.out.println(customCaesarCipher(1, "All the Best"));
        // Output: The encrypted Text is: Bmm uif Cftu
        System.out.println(customCaesarCipher(2, "Hello 123"));
        // Output: The encrypted Text is: Jgnnq 345
    }
}
```

#### C++
```cpp
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
    cout << customCaesarCipher(1, "All the Best") << endl;
    cout << customCaesarCipher(2, "Hello 123") << endl;
    return 0;
}
```

#### Python
```python
def custom_caesar_cipher(key, message):
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

# Test
if __name__ == "__main__":
    print(custom_caesar_cipher(1, "All the Best"))
    # Output: The encrypted Text is: Bmm uif Cftu
    print(custom_caesar_cipher(2, "Hello 123"))
    # Output: The encrypted Text is: Jgnnq 345
```

---

### Approach 2: Using Helper Functions

#### Java
```java
public class CaesarCipherHelper {
    private static char encryptChar(char c, int key) {
        char base = Character.isUpperCase(c) ? 'A' : 'a';
        return (char) ((c - base + key) % 26 + base);
    }
    
    private static char encryptDigit(char c, int key) {
        int digit = Character.getNumericValue(c);
        return (char) ('0' + (digit + key) % 10);
    }
    
    public static String customCaesarCipher(int key, String message) {
        if (key < 0) {
            return "INVALID INPUT";
        }
        
        StringBuilder encrypted = new StringBuilder();
        
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                encrypted.append(encryptChar(c, key));
            } else if (Character.isDigit(c)) {
                encrypted.append(encryptDigit(c, key));
            } else {
                encrypted.append(c);
            }
        }
        
        return "The encrypted Text is: " + encrypted.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(customCaesarCipher(1, "All the Best"));
    }
}
```

#### C++
```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

char encryptChar(char c, int key) {
    char base = isupper(c) ? 'A' : 'a';
    return (char)((c - base + key) % 26 + base);
}

char encryptDigit(char c, int key) {
    int digit = c - '0';
    return (char)('0' + (digit + key) % 10);
}

string customCaesarCipher(int key, string message) {
    if (key < 0) {
        return "INVALID INPUT";
    }
    
    string encrypted = "";
    
    for (char c : message) {
        if (isalpha(c)) {
            encrypted += encryptChar(c, key);
        } else if (isdigit(c)) {
            encrypted += encryptDigit(c, key);
        } else {
            encrypted += c;
        }
    }
    
    return "The encrypted Text is: " + encrypted;
}

int main() {
    cout << customCaesarCipher(1, "All the Best") << endl;
    return 0;
}
```

#### Python
```python
def encrypt_char(c, key):
    base = ord('A') if c.isupper() else ord('a')
    return chr((ord(c) - base + key) % 26 + base)

def encrypt_digit(c, key):
    digit = int(c)
    return str((digit + key) % 10)

def custom_caesar_cipher(key, message):
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

# Test
if __name__ == "__main__":
    print(custom_caesar_cipher(1, "All the Best"))
```

---

### Approach 3: Using Lambda & Map Functions

#### Java
```java
import java.util.function.Function;

public class CaesarCipherLambda {
    public static String customCaesarCipher(int key, String message) {
        if (key < 0) {
            return "INVALID INPUT";
        }
        
        Function<Character, Character> processChar = c -> {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                return (char) ((c - base + key) % 26 + base);
            } else if (Character.isDigit(c)) {
                int digit = Character.getNumericValue(c);
                return (char) ('0' + (digit + key) % 10);
            }
            return c;
        };
        
        StringBuilder encrypted = new StringBuilder();
        message.chars().forEach(ch -> encrypted.append(processChar.apply((char)ch)));
        
        return "The encrypted Text is: " + encrypted.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(customCaesarCipher(1, "All the Best"));
    }
}
```

#### Python
```python
def custom_caesar_cipher(key, message):
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

# Test
if __name__ == "__main__":
    print(custom_caesar_cipher(1, "All the Best"))
```

---

### Approach 4: Using List Comprehension (Python) / Streams (Java)

#### Python
```python
def custom_caesar_cipher(key, message):
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

# Compact one-liner version
def custom_caesar_cipher_oneliner(key, message):
    if key < 0:
        return "INVALID INPUT"
    return "The encrypted Text is: " + ''.join(
        chr((ord(c) - (ord('A') if c.isupper() else ord('a')) + key) % 26 + (ord('A') if c.isupper() else ord('a'))) if c.isalpha() else
        str((int(c) + key) % 10) if c.isdigit() else
        c for c in message
    )

# Test
if __name__ == "__main__":
    print(custom_caesar_cipher(1, "All the Best"))
```

#### Java Streams
```java
public class CaesarCipherStreams {
    public static String customCaesarCipher(int key, String message) {
        if (key < 0) {
            return "INVALID INPUT";
        }
        
        String encrypted = message.chars()
            .mapToObj(ch -> {
                char c = (char) ch;
                if (Character.isLetter(c)) {
                    char base = Character.isUpperCase(c) ? 'A' : 'a';
                    return String.valueOf((char) ((c - base + key) % 26 + base));
                } else if (Character.isDigit(c)) {
                    int digit = Character.getNumericValue(c);
                    return String.valueOf((digit + key) % 10);
                }
                return String.valueOf(c);
            })
            .reduce("", String::concat);
        
        return "The encrypted Text is: " + encrypted;
    }
    
    public static void main(String[] args) {
        System.out.println(customCaesarCipher(1, "All the Best"));
    }
}
```

---

## Complete Test Suite

### Java Test Class
```java
public class TestAll {
    public static void main(String[] args) {
        System.out.println("=== WASHING MACHINE TESTS ===");
        System.out.println(WashingMachine.getTimeEstimate(0));      // 0 Minutes
        System.out.println(WashingMachine.getTimeEstimate(2000));   // 25 Minutes
        System.out.println(WashingMachine.getTimeEstimate(2001));   // 35 Minutes
        System.out.println(WashingMachine.getTimeEstimate(4000));   // 35 Minutes
        System.out.println(WashingMachine.getTimeEstimate(4001));   // 45 Minutes
        System.out.println(WashingMachine.getTimeEstimate(7000));   // 45 Minutes
        System.out.println(WashingMachine.getTimeEstimate(7001));   // OVERLOADED!
        System.out.println(WashingMachine.getTimeEstimate(-1));     // INVALID INPUT
        
        System.out.println("\n=== CAESAR CIPHER TESTS ===");
        System.out.println(CaesarCipher.customCaesarCipher(1, "All the Best"));
        System.out.println(CaesarCipher.customCaesarCipher(2, "Hello 123"));
        System.out.println(CaesarCipher.customCaesarCipher(25, "ABC xyz 789"));
        System.out.println(CaesarCipher.customCaesarCipher(-1, "Test"));  // INVALID INPUT
    }
}
```

### Python Test File
```python
# test_all.py

from washing_machine import get_time_estimate
from caesar_cipher import custom_caesar_cipher

print("=== WASHING MACHINE TESTS ===")
print(get_time_estimate(0))        # 0 Minutes
print(get_time_estimate(2000))     # 25 Minutes
print(get_time_estimate(2001))     # 35 Minutes
print(get_time_estimate(4000))     # 35 Minutes
print(get_time_estimate(4001))     # 45 Minutes
print(get_time_estimate(7000))     # 45 Minutes
print(get_time_estimate(7001))     # OVERLOADED!
print(get_time_estimate(-1))       # INVALID INPUT

print("\n=== CAESAR CIPHER TESTS ===")
print(custom_caesar_cipher(1, "All the Best"))
print(custom_caesar_cipher(2, "Hello 123"))
print(custom_caesar_cipher(25, "ABC xyz 789"))
print(custom_caesar_cipher(-1, "Test"))  # INVALID INPUT
```

---

## Summary of Approaches

### Washing Machine
1. **Approach 1**: Simple if-else (Most readable, beginner-friendly)
2. **Approach 2**: Range map (Scalable, maintainable)
3. **Approach 3**: Ternary operators (Compact, functional)

### Caesar Cipher
1. **Approach 1**: Simple iteration (Clear logic)
2. **Approach 2**: Helper functions (Better organization)
3. **Approach 3**: Lambda/Map functions (Functional programming)
4. **Approach 4**: List comprehension/Streams (Modern, concise)

Choose based on your coding style and project requirements!
