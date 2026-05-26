#include <iostream> 
#include <vector> 
#include <utility> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size(); 
        vector<pair<int, int>> pos(n, make_pair(0, 0)); 
        for (int i = 0; i < n; i++) {
            pos[i].first = positions[i]; 
            pos[i].second = i; 
        }
        sort(pos.begin(), pos.end()); 
        vector<pair<int, int>> stk = {};
        vector<bool> surv(n, true); 
        for (auto& v: pos) {
            int p = v.first, i = v.second; 
            int h = healths[i]; 
            char d = directions[i]; 
            if (d == 'L') {
                while ((stk.size() > 0) && (healths[i] > 0)) {
                    int _h = stk.back().first, _i = stk.back().second; 
                    if (h > _h) {
                        surv[_i] = false; 
                        stk.pop_back(); 
                        healths[i]--; 
                        h--; 
                    }
                    else if (h < _h) {
                        surv[i] = false; 
                        healths[_i]--; 
                        stk.back().first--; 
                        break; 
                    }
                    else {
                        surv[_i] = false; 
                        surv[i] = false; 
                        stk.pop_back(); 
                        break; 
                    }
                }
            }
            else 
                stk.push_back(make_pair(h, i)); 
        }
        vector<int> h = {}; 
        for (int i = 0; i < n; i++) {
            if (surv[i])
                h.push_back(healths[i]); 
        }
        return h; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> positions = {5,4,3,2,1}; 
    // vector<int> healths = {2,17,9,15,10}; 
    // string directions = "RRRRR"; 
    vector<int> positions = {3,5,2,6}; 
    vector<int> healths = {10,10,15,12}; 
    string directions = "RLRL"; 
    vector<int> ret = s.survivedRobotsHealths(positions, healths, directions); 
    cout << "ans: " << endl; 
    for (auto x: ret)
        cout << x << " "; 
    cout << endl; 
}