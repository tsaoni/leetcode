#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <utility> 

using namespace std; 
class Solution {
public:
    int get_n_walls_per_itvl(vector<int>& walls, int lv, int rv) {
        int m = walls.size(); 
        int l = 0, r = m - 1; 
        int val = lv; 
        while (l < r) {
            int mid = (l + r + 1) / 2; 
            if (walls[mid] >= val)
                r = mid - 1; 
            else 
                l = mid; 
        }
        int _l = (walls[l] < lv) ? l : -1; 
        // cout << _l << endl; 

        l = 0, r = m - 1; 
        val = rv; 
        while (l < r) {
            int mid = (l + r + 1) / 2; 
            if (walls[mid] > val)
                r = mid - 1; 
            else 
                l = mid; 
        }
        l = (walls[l] <= rv) ? l : -1; 
        // cout << l << endl; 
    
        return l - _l; 
    }

    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        int n = robots.size(); 
        vector<pair<int, int>> rpos = {}; 
        for (int i = 0; i < n; i++)
            rpos.push_back(make_pair(robots[i], i)); 
        sort(rpos.begin(), rpos.end()); 
        sort(walls.begin(), walls.end()); 
    
        int ret = 0; 
        vector<vector<int>> dp(n, vector<int>(2, 0)); 
        int lp = rpos[0].first - distance[rpos[0].second], rp = rpos[0].first + distance[rpos[0].second]; 
        if (n > 1)
            rp = min(rp, rpos[1].first - 1); 
        int l_n_walls = get_n_walls_per_itvl(walls, lp, rpos[0].first); 
        // cout << lp << " " << rpos[0].first << endl; 
        int r_n_walls = get_n_walls_per_itvl(walls, rpos[0].first, rp); 
        // cout << rpos[0].first << " " << rp << endl; 
        dp[0][0] = l_n_walls; 
        dp[0][1] = r_n_walls; 

        for (int i = 1; i < n; i++) {
            
            lp = max(rpos[i - 1].first + 1, rpos[i].first - distance[rpos[i].second]); 
            int _lp = max(lp, rpos[i - 1].first + distance[rpos[i - 1].second] + 1); 
            if (i == n - 1)
                rp = rpos[i].first + distance[rpos[i].second]; 
            else
                rp = min(rpos[i + 1].first - 1, rpos[i].first + distance[rpos[i].second]); 
            
            int l_n_walls = get_n_walls_per_itvl(walls, lp, rpos[i].first); 
            int _l_n_walls = get_n_walls_per_itvl(walls, _lp, rpos[i].first); 
            dp[i][0] = max(dp[i - 1][0] + l_n_walls, dp[i - 1][1] + _l_n_walls); 
            int r_n_walls = get_n_walls_per_itvl(walls, rpos[i].first, rp); 
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + r_n_walls; 
        }
        // for (auto& p: dp)
        //     cout << p[0] << " " << p[1] << endl; 
        // cout << endl; 
        return max(dp[n - 1][0], dp[n - 1][1]); 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> robots = {4}, distance = {3}, walls = {1,10}; 
    // vector<int> robots = {10,2}, distance = {5,1}, walls = {5,2,7}; 
    vector<int> robots = {1,2}, distance = {100,1}, walls = {10}; 
    int ret = s.maxWalls(robots, distance, walls); 
    cout << "ans: " << ret << endl; 
}