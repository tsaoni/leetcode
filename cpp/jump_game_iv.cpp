#include <iostream> 
#include <vector> 
#include <queue> 
#include <unordered_map> 
#include <unordered_set> 

using namespace std; 
class Solution {
public:
    int minJumps(vector<int>& arr) {
        unordered_map<int, unordered_set<int>> mp; 
        vector<int> steps(arr.size(), 0); 
        for (int i = 0; i < arr.size(); i++) {
            if (mp.find(arr[i]) == mp.end())
                mp[arr[i]] = unordered_set<int>(); 
            mp[arr[i]].insert(i); 
        }

        queue<int> q; 
        q.push(0); 
        steps[0] = 0; 
        while (q.size() > 0) {
            int cur = q.front(); 
            if (cur == arr.size() - 1)
                return steps[cur]; 
            q.pop(); 
            if (cur > 0) {
                if (mp[arr[cur - 1]].find(cur - 1) != mp[arr[cur - 1]].end()) {
                    q.push(cur - 1); 
                    mp[arr[cur - 1]].erase(cur - 1); 
                    steps[cur - 1] = steps[cur] + 1; 
                }
            }
            if (cur < arr.size() - 1) {
                if (mp[arr[cur +1]].find(cur + 1) != mp[arr[cur + 1]].end()) {
                    q.push(cur + 1); 
                    mp[arr[cur + 1]].erase(cur + 1); 
                    steps[cur + 1] = steps[cur] + 1; 
                }
            }
            for (auto x: mp[arr[cur]]) {
                if (cur != x) {
                    q.push(x); 
                    steps[x] = steps[cur] + 1; 
                }
                
            }
            mp[arr[cur]] = unordered_set<int>(); 
                
        }
        return -1; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<int> arr = {7,6,9,6,9,6,9,7}; 
    int ret = s.minJumps(arr); 
    cout << "ans: " << ret << endl; 
}