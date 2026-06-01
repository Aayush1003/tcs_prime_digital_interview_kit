/**
 * TCS NQT 2020 - Washing Machine Problem
 * Approach 1: Simple If-Else Logic
 */

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
        System.out.println("=== WASHING MACHINE TEST ===");
        System.out.println("Input: 0       -> " + getTimeEstimate(0));
        System.out.println("Input: 2000    -> " + getTimeEstimate(2000));
        System.out.println("Input: 2001    -> " + getTimeEstimate(2001));
        System.out.println("Input: 4000    -> " + getTimeEstimate(4000));
        System.out.println("Input: 4001    -> " + getTimeEstimate(4001));
        System.out.println("Input: 7000    -> " + getTimeEstimate(7000));
        System.out.println("Input: 7001    -> " + getTimeEstimate(7001));
        System.out.println("Input: -100    -> " + getTimeEstimate(-100));
    }
}
