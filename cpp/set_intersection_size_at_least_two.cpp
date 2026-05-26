#include <iostream> 
#include <algorithm>
#include <vector>

using namespace std; 
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        int prev1 = -1, prev2 = -1; 
        int ret = 0; 
        sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });

        for (auto& v: intervals) {
            int start = v[0], end = v[1]; 
            if (prev2 < start) {
                prev2 = end, prev1 = end - 1; 
                // cout << prev1 << " " << prev2 << endl; 
                ret += 2; 
            }
            else {
                if (prev1 < start) {
                    if (prev2 == end) {
                        prev1 = end - 1; 
                    }
                    else {
                        prev1 = prev2; 
                        prev2 = end;
                    }
                     
                    // cout << prev1 << " " << prev2 << endl; 
                    ret++; 
                }
            }
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> intervals = {{1,3},{3,7},{5,7},{7,8}}; 
    int ans = s.intersectionSizeTwo(intervals); 
    cout << "ans: " << ans << endl; 
    return 0; 
}