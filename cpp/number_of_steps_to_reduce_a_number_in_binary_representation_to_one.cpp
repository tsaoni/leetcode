#include <iostream>
#include <string>

using namespace std; 

class Solution {
public:
    int numSteps(string s) {
        int n_ops = 0, c = 0; 
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == '1' && c == 1) {
                n_ops++; 
            }
            else if ((s[i] == '0' && c == 1) || (s[i] == '1' && c == 0)) {
                if (i == 0) break; 
                n_ops += 2; 
                c = 1; 
            }
            else 
                n_ops++; 
        }
        return n_ops; 
    }
};

int main() {
    Solution sol = Solution(); 
    // string s = "1101"; 
    // string s = "10"; 
    string s = "1"; 
    int ret = sol.numSteps(s); 
    cout << "ans: " << ret << endl; 
    return 0; 
}