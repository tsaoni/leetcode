#include <iostream> 
#include <vector> 
#include <queue> 
#include <functional> 

using namespace std; 
class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        priority_queue<int> max_hp;
        priority_queue<int, vector<int>, greater<int>> min_hp;
        long long _mass = mass; 
        for (int x: asteroids) {
            if (mass >= x)
                max_hp.push(x); 
            else 
                min_hp.push(x); 
        }
        while (!min_hp.empty()) {
            if (min_hp.top() <= _mass) {
                _mass += static_cast<long long>(min_hp.top()); 
                min_hp.pop(); 
            }
            else {
                if (!max_hp.empty()) {
                    _mass += static_cast<long long>(max_hp.top()); 
                    max_hp.pop(); 
                }
                else {
                    return false; 
                }
            }
        }
        return true; 
    }
};