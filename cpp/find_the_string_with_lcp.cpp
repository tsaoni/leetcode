#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    string findTheString(vector<vector<int>>& lcp) {
        string w = ""; 
        int n = lcp.size(); 
        char c = 'a'; 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // cout << i << " " << j << " " << lcp[i][j] << endl; 
                if (lcp[i][j] > 0) {
                    w += w[j]; 
                    break; 
                }
            }
            if (w.size() == i) {
                if (c > 'z') 
                    return ""; 
                w += c; 
                c++; 
            }
        }
        // cout << w << endl; 
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i == (n - 1) || j == (n - 1)) {
                    if (!((w[i] == w[j]) && (lcp[i][j] == 1)) && !((w[i] != w[j]) && (lcp[i][j] == 0)))
                        return ""; 
                }
                else {
                    if (w[i] == w[j]) {
                        if (!(lcp[i][j] == (lcp[i + 1][j + 1] + 1)))
                            return ""; 
                    }
                    else {
                        if (!(lcp[i][j] == 0))
                            return ""; 
                    }
                }
            }
        }
        return w; 
    }
};

int main() {
    vector<vector<int>> lcp = {{4,0,2,0},{0,3,0,1},{2,0,2,0},{0,1,0,1}}; 
    Solution s = Solution(); 
    string w = s.findTheString(lcp); 
    cout << "ans: " << w << endl; 
    return 0; 
}