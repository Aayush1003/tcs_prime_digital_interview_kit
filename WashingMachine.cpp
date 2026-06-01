/*
 * TCS NQT 2020 - Washing Machine Problem
 * Approach 1: Simple If-Else Logic
 */

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
    cout << "=== WASHING MACHINE TEST ===" << endl;
    cout << "Input: 0       -> " << getTimeEstimate(0) << endl;
    cout << "Input: 2000    -> " << getTimeEstimate(2000) << endl;
    cout << "Input: 2001    -> " << getTimeEstimate(2001) << endl;
    cout << "Input: 4000    -> " << getTimeEstimate(4000) << endl;
    cout << "Input: 4001    -> " << getTimeEstimate(4001) << endl;
    cout << "Input: 7000    -> " << getTimeEstimate(7000) << endl;
    cout << "Input: 7001    -> " << getTimeEstimate(7001) << endl;
    cout << "Input: -100    -> " << getTimeEstimate(-100) << endl;
    
    return 0;
}
