#include <iostream> 
#include <cmath> 
#include <string> 

using namespace std; 

class Solution {
public:
    char findKthBit(int n, int k) {
        int n_bits = pow(2, n) - 1; 
        int cur = 1; 
        int n_change = 0; 
        int cnt = 0; 
        while (cur <= n_bits) {
            // cout << cur << "k" << k << "k" << n_change << endl; 
            int mid = (cur + n_bits) / 2; 
            if (mid == k) {
                if (cnt == 0) {
                    int final_c = (mid == n_bits)? 0: 1; 
                    // cout << "h" << endl; 
                    return to_string(final_c)[0]; 
                }
                else {
                    n_change++; 
                    int final_c = (mid == n_bits)? 0: 1; 
                    // cout << final_c << endl; 
                    final_c = (final_c + n_change) % 2; 
                    // cout << cur << " " << n_change << endl; 
                    return to_string(final_c)[0]; 
                }

            }
            else if (k < mid) {
                k = (2 * mid) - k; 
                n_change++;  
            }
            cur = mid + 1; 
            cnt++; 
        }
        return '-'; 
    }
};

int main() {
    Solution s = Solution(); 
    // int n = 2, k = 3; 
    // int n = 4, k = 11; 
    int n = 1, k = 1; 
    char ret = s.findKthBit(n, k); 
    cout << "ans: " << ret << endl; 
    return 0; 
}