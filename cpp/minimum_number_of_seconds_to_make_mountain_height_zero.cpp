#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <cmath> 

using namespace std; 
class Solution {
public:
    static bool search(long v, int h, vector<int>& t) {
        long work, k, _h = 0; 
        for (auto _t: t) {
            work = v / _t; 
            k = floor((sqrt(1 + 8 * work) - 1) / 2); 
            // v -= ((1 + k) * k / 2 * _t); 
            _h += k; 
            // cout << _h << " " << v << endl; 
            if (_h >= h) 
                return true; 
        }
        // cout << _h << endl; 
        return false; 
    }

    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        // sort(workerTimes.begin(), workerTimes.end()); 
        long l = 0, r = workerTimes[0] * ((static_cast<long>(1 + mountainHeight) * static_cast<long>(mountainHeight)) / 2L); 
        bool x = search(3, mountainHeight, workerTimes); 
        // cout << r << "h " << x << endl; 
        while (l < r) {
            long mid = (l + r) / 2L; 
            if (search(mid, mountainHeight, workerTimes))
                r = mid; 
            else 
                l = mid + 1; 
        }
        return l; 
    }
};

int main() {
    Solution s = Solution(); 
    // int mountainHeight = 4; 
    // vector<int> workerTimes = {2,1,1}; 
    // int mountainHeight = 10; 
    // vector<int> workerTimes = {3,2,2,4}; 
    int mountainHeight = 5; 
    vector<int> workerTimes = {1}; 
    int ret = s.minNumberOfSeconds(mountainHeight, workerTimes); 
    cout << "ans: " << ret << endl; 
}