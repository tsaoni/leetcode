#include <iostream> 
#include <vector> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> l = {}; 
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++)
                l.push_back(grid[i][j]); 
        }
        sort(l.begin(), l.end()); 
        int ret = 0; 
        for (int i = 0; i < l.size(); i++)
            ret += (l[i] - l[0]); 
        int cur = ret; 
        int n = l.size(); 
        for (int i = 1; i < l.size(); i++) {
            int dist = l[i] - l[i - 1]; 
            if (dist % x != 0)
                return -1; 
            cur += ((2 * i - n) * dist); 
            ret = min(ret, cur); 
        }
        return ret; 
    }
};