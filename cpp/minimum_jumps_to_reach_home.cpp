#include <vector> 
#include <iostream> 

using namespace std; 
class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        int bound = 10000; //max(*max_element(forbidden.begin(), forbidden.end()) + a + b, x + b); 
        vector<int> arrived(bound + 1, 2); 
        vector<int> q = {0}, _q = {}; 
        vector<int>& p = q, _p = _q; 
        for (int i = 0; i < b; i++)
            arrived[i] = 1; 
        for (int i = bound - a + 1; i <= bound; i++)
            arrived[i] = -1; 
        for (int pos: forbidden)
            arrived[pos] = 0; 
        int step = 0; 
        while (!p.empty()) {
            for(int i = 0; i < p.size(); i++) {
                int pos = p[i]; 
                if (pos == x)
                    return step; 
                // p.erase(p.begin()); 
                
                bool pos_neg = false; 
                if ((arrived[pos] > 0) && ((pos + a) <= bound)) {
                    if (arrived[pos + a] != 0)
                        _p.push_back(pos + a); 
                    if (arrived[pos] != 1)
                        arrived[pos] = -1; 
                    else 
                        pos_neg = true; 
                }
                if ((arrived[pos] == -1) && ((pos - b) >= 0)) {
                    if (arrived[pos - b] > 0) {
                        _p.push_back(pos - b); 
                        arrived[pos] = 0; 
                        if(arrived[pos - b] == 2)
                            arrived[pos - b] = 1; 
                    } 
                    if (arrived[pos - b] == 0) 
                        arrived[pos] = 0; 
                }
                if (pos_neg)
                    arrived[pos] = -1; 
            }
            swap(_p, p); 
            _p = {}; 
            step++; 
        }
        return -1; 
    }
};