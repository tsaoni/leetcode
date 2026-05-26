#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    void dfs(vector<int>& arr, vector<int>& dp, int cur, int d) {
        if (dp[cur] > 0)
            return; 
        int N = arr.size(); 
        int start = max(0, cur - d), end = min(N - 1, cur + d); 
        for (int i = cur - 1; i >= start; i--) {
            if (arr[i] >= arr[cur])
                break; 
            dfs(arr, dp, i, d); 
            dp[cur] = max(dp[cur], dp[i] + 1); 
        }
        for (int i = cur + 1; i <= end; i++) {
            if (arr[i] >= arr[cur])
                break; 
            dfs(arr, dp, i, d); 
            dp[cur] = max(dp[cur], dp[i] + 1); 
        }
        if (dp[cur] < 0)
            dp[cur] = 1; 
    }

    int maxJumps(vector<int>& arr, int d) {
        int N = arr.size(); 
        vector<int> dp(N, -1); 
        int ret = 1; 
        for (int i = 0; i < N; i++) {
            dfs(arr, dp, i, d); 
            ret = max(dp[i], ret); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> arr = {6,4,14,6,8,13,9,7,10,6,12}; 
    // int d = 2; 
    // vector<int> arr = {3,3,3,3,3}; 
    // int d = 3; 
    vector<int> arr = {37,6,5,4,3,2,1}; 
    int d = 1; 
    int ret = s.maxJumps(arr, d); 
    cout << "ans: " << ret << endl; 
}