#include <iostream> 
#include <vector> 
#include <cmath> 
#include <unordered_map> 
#include <queue> 

using namespace std; 
class Solution {
public:
    vector<bool> find_primes(int n) {
        vector<bool> is_prime(n, true); 
        is_prime[0] = false; 
        for (int i = 1; i < n; i++) {
            if (is_prime[i]) {
                // for (int j = 2; j < static_cast<int>(sqrt(i + 1)) + 1; j++) {
                //     if ((i + 1) % (j) == 0) {
                //         is_prime[i] = false; 
                //         break; 
                //     }
                // }
                // if (is_prime[i]) {
                for (int _i = 2 * (i + 1); _i < n + 1; _i += (i + 1)) {
                    is_prime[_i - 1] = false; 
                    // cout << _i << endl; 
                }
                // }
            }
        }
        // for (auto x: is_prime)
        //     cout << x << " "; 
        // cout << endl; 
        return is_prime; 
    }

    int minJumps(vector<int>& nums) {
        int max_n = nums[0]; 
        int n = nums.size(); 
        for (int x: nums)
            max_n = max(x, max_n); 
        vector<bool> is_prime = find_primes(max_n); 
        unordered_map<int, vector<int>> mp; 
        // for (int i = 0; i < n; i++) {
        //     if (is_prime[nums[i] - 1] && (mp.find(nums[i]) == mp.end())) {
        //         mp[nums[i]] = {}; 
        //         for (int j = 0; j < n; j++) {
        //             if (nums[j] % nums[i] == 0)
        //                 mp[nums[i]].push_back(j); 
        //         }
        //     }
        // }
        
        for (int i = 0; i < n; i++) {
            if (mp.find(nums[i]) == mp.end()) {
                mp[nums[i]] = {}; 
            }
            mp[nums[i]].push_back(i); 
        }
        for (auto& [num, pos] : mp) {
            if (is_prime[num - 1]) {
                for (int x = 2 * num; x < max_n + 1; x += num) {
                    if (mp.find(x) != mp.end()) {
                        for (auto _x: mp[x])
                            pos.push_back(_x); 
                    }
                }
            }
        }

        vector<int> steps(n, -1); 
        queue<int> q; 
        q.push(0); 
        steps[0] = 0; 
        while (steps[n - 1] < 0) {
            int cur = q.front(); 
            q.pop(); 
            if (cur > 0 && steps[cur - 1] < 0) {
                steps[cur - 1] = steps[cur] + 1; 
                q.push(cur - 1); 
            }
            if (cur < n - 1 && steps[cur + 1] < 0) {
                steps[cur + 1] = steps[cur] + 1; 
                q.push(cur + 1); 
            }
            if (is_prime[nums[cur] - 1]) {
                for (int nxt: mp[nums[cur]]) {
                    if (steps[nxt] < 0) {
                        steps[nxt] = steps[cur] + 1; 
                        q.push(nxt); 
                    }
                }
                mp[nums[cur]] = {}; 
            }
            
        }

        return steps[n - 1]; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> nums = {1,2,4,6}; 
    // vector<int> nums = {2,3,4,7,9}; 
    vector<int> nums = {4,6,5,8}; 
    int ret = s.minJumps(nums); 
    cout << "ans: " << ret << endl; 
}