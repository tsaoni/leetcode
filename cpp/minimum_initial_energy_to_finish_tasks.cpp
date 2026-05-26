#include <iostream> 
#include <vector> 
#include <utility> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        vector<pair<int, int>> tb; 
        for (int i = 0; i < tasks.size(); i++)
            tb.push_back(make_pair(tasks[i][1] - tasks[i][0], i)); 
        sort(tb.begin(), tb.end()); 
        int ret = tasks[tb[0].second][1]; 
        // for (auto p: tb)
        //     cout << p.first << " " << p.second << endl; 
        for (int i = 1; i < tasks.size(); i++) {
            ret += tasks[tb[i].second][0]; 
            if (tasks[tb[i].second][1] > ret)
                ret = tasks[tb[i].second][1]; 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<vector<int>> tasks = {{1,2},{2,4},{4,8}}; 
    int ret = s.minimumEffort(tasks); 
    cout << "ans: " << ret << endl; 
}