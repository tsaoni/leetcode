#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        vector<int> L(2 * limit + 1, 0); 
        int N = nums.size(); 
        for (int i = 0; i < N / 2; i++) {
            int a = nums[i], b = nums[N - i - 1]; 
            if (a > b)
                swap(a, b); 
            L[2 * limit] += 2; 
            L[b + limit]--; 
            L[a]++; 
            L[a + b]--; 
            L[a + b - 1]++; 
            // int x1, x2, x3, x4, x5; 
            // if (a > 1)
            // x1 = 2; 
            // else if (a == 1 && b > 1)
            //     x1 = 1; 
            // else 
            //     x1 = 0; 
            // if (b > 1)
            // x2 = 1; 
            // else 
            //     x2 = 0; 
            // x3 = 0; 
            // if (a < limit)
            // x4 = 1; 
            // else 
            //     x4 = 0; 
            // if (b < limit)
            // x5 = 2; 
            // else if (b == limit && a < limit)
            //     x5 = 1; 
            // else 
            //     x5 = 0; 
            
            
            // L[2 * limit] += x5; 
            // if (b < limit)
            // L[b + limit] += x4 - x5; 
            // if (a < limit)
            // L[a + b] += x3 - x4; 
            // if (b > 1)
            // L[a + 1] += x2 - x3; 
            // if (a > 1)
            // L[2] += x1 - x2; 
        }
        int ret = L[2 * limit]; 
        for (int i = L.size() - 1; i > 0; i--) {
            L[i - 1] += L[i]; 
            // cout << L[i - 1] << endl; 
            ret = min(L[i - 1], ret); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {1,2,4,3}; 
    // int limit = 4; 
    vector<int> nums = {1,2,2,1}; 
    int limit = 2; 
    int ret = s.minMoves(nums, limit); 
    cout << "ans: " << ret << endl; 
}