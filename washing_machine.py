"""
TCS NQT 2020 - Washing Machine Problem
Multiple Approaches
"""

# ============================================
# APPROACH 1: Simple If-Else Logic
# ============================================
def get_time_estimate_v1(weight):
    """Simple if-else approach"""
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


# ============================================
# APPROACH 2: Using Ranges/Tuples (Cleaner)
# ============================================
def get_time_estimate_v2(weight):
    """Using ranges for scalability"""
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


# ============================================
# APPROACH 3: Ternary/Conditional Expression
# ============================================
def get_time_estimate_v3(weight):
    """Functional style using nested ternary operators"""
    return ("INVALID INPUT" if weight < 0 else
            "Time Estimated: 0 Minutes" if weight == 0 else
            "OVERLOADED!" if weight > 7000 else
            "Time Estimated: 25 Minutes" if weight <= 2000 else
            "Time Estimated: 35 Minutes" if weight <= 4000 else
            "Time Estimated: 45 Minutes")


# ============================================
# APPROACH 4: Using Dictionary with Function
# ============================================
def get_time_estimate_v4(weight):
    """Using dictionary for lookup"""
    if weight < 0:
        return "INVALID INPUT"
    
    if weight == 0:
        return "Time Estimated: 0 Minutes"
    
    if weight > 7000:
        return "OVERLOADED!"
    
    time_map = {
        (1, 2000): 25,
        (2001, 4000): 35,
        (4001, 7000): 45
    }
    
    for (min_w, max_w), time in time_map.items():
        if min_w <= weight <= max_w:
            return f"Time Estimated: {time} Minutes"
    
    return "INVALID INPUT"


# ============================================
# APPROACH 5: Using Binary Search (Advanced)
# ============================================
def get_time_estimate_v5(weight):
    """Using ranges with lambda functions"""
    if weight < 0:
        return "INVALID INPUT"
    
    if weight == 0:
        return "Time Estimated: 0 Minutes"
    
    if weight > 7000:
        return "OVERLOADED!"
    
    # Define ranges and times
    ranges = [(2000, 25), (4000, 35), (7000, 45)]
    
    for limit, time in ranges:
        if weight <= limit:
            return f"Time Estimated: {time} Minutes"
    
    return "INVALID INPUT"


# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    test_cases = [0, 2000, 2001, 4000, 4001, 7000, 7001, -1]
    
    print("=" * 60)
    print("WASHING MACHINE - ALL APPROACHES")
    print("=" * 60)
    
    for weight in test_cases:
        print(f"\nInput: {weight}")
        print(f"  Approach 1: {get_time_estimate_v1(weight)}")
        print(f"  Approach 2: {get_time_estimate_v2(weight)}")
        print(f"  Approach 3: {get_time_estimate_v3(weight)}")
        print(f"  Approach 4: {get_time_estimate_v4(weight)}")
        print(f"  Approach 5: {get_time_estimate_v5(weight)}")
