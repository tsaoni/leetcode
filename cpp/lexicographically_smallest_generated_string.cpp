#include <iostream> 
#include <vector> 
#include <string> 

using namespace std; 
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size(); 
        string s(n + m - 1, 'a'); 
        vector<bool> fixed(n + m - 1, false); 
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    if (!fixed[j + i])
                        s[j + i] = str2[j]; 
                    else if (s[j + i] != str2[j])
                        return ""; 
                    fixed[j + i] = true; 
                }
            }
        }
        // cout << "here" << endl; 
        // for (auto x: s)
        //     cout << x << " "; 
        // cout << endl; 
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool is_set = false; 
                for (int j = 0; j < m; j++) {
                    if (s[i + j] != str2[j])
                        is_set = true; 
                }
                if (!is_set) {
                    for (int j = m - 1; j >= 0; j--) {
                        if (!fixed[i + j]) {
                            if (s[i + j] != 'z') {
                                s[i + j]++; 
                                is_set = true; 
                                break; 
                            }
                        }
                    }
                }
                if (!is_set)
                    return ""; 
            }
        }
        return s; 
    }
};

int main() {
    Solution s = Solution(); 
    // string str1 = "TFTF", str2 = "ab"; 
    // string str1 = "TFTF", str2 = "abc"; 
    string str1 = "F", str2 = "d"; 
    string ret = s.generateString(str1, str2); 
    cout << "ans: " << ret << endl; 
}