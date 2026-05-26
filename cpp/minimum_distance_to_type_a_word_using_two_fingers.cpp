#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int minimumDistance(string word) {
        int MAX_VAL = 2400; 
        vector<vector<int>> dist(26, vector<int>(26, 0)); 
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i][j] = abs(i / 6 - j / 6) + abs(i % 6 - j % 6); 
            }
        }
        vector<vector<int>> _dp(2, vector<int>(27, -1)), dp(2, vector<int>(27, -1)); 
        vector<vector<int>>& _p = _dp, p = dp; 
        
        char prev = '0'; 
        for (char c: word) {
            if (prev == c)
                continue; 
            // cout << "hh" << endl; 
            if (prev == '0')
                p[0][0] = p[1][0] = 0; 
            else {
                int pidx = prev - 'A', idx = c - 'A'; 
                for (int i = 0; i < 27; i++) {
                    if (_p[0][i] >= 0)
                        p[0][i] = _p[0][i] + dist[pidx][idx]; 
                    if (_p[1][i] >= 0)
                        p[1][i] = _p[1][i] + dist[pidx][idx]; 
                }
                p[0][pidx + 1] = (p[0][pidx + 1] < 0) ? _p[1][0]: min(p[0][pidx + 1], _p[1][0]); 
                p[1][pidx + 1] = (p[1][pidx + 1] < 0) ? _p[0][0]: min(p[1][pidx + 1], _p[0][0]); 
                for (int i = 1; i < 27; i++) {
                    if (_p[1][i] >= 0)
                        p[0][pidx + 1] = (p[0][pidx + 1] < 0) ? _p[1][i] + dist[i - 1][idx]: min(p[0][pidx + 1], _p[1][i] + dist[i - 1][idx]); 
                    if (_p[0][i] >= 0)
                        p[1][pidx + 1] = (p[1][pidx + 1] < 0) ? _p[0][i] + dist[i - 1][idx]: min(p[1][pidx + 1], _p[0][i] + dist[i - 1][idx]); 
                }
            }
            
            prev = c; 
            swap(_p, p); 
            // for (int i = 0; i < 2; i++) {
            //     for (int j = 0; j < 27; j++)
            //         cout << _p[i][j] << " ";
            //     cout << endl; 
            // }
            // cout << endl; 
        }
        int ret = MAX_VAL; 
        for (int i = 0; i < 27; i++) {
            ret = (_p[0][i] >= 0) ? min(_p[0][i], ret): ret; 
            ret = (_p[1][i] >= 0) ? min(_p[1][i], ret): ret; 
        }
        
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    string word = "CAKE"; 
    // string word = "HAPPY"; 
    int ret = s.minimumDistance(word); 
    cout << "ans: " << ret << endl; 
}