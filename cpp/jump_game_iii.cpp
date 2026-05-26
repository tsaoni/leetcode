#include <iostream> 
#include <vector>
#include <queue> 

using namespace std; 
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int N = arr.size(); 
        queue<int> q; 
        q.push(start); 
        while (q.size() > 0) {
            int x = q.front(); 
            q.pop(); 
            if (arr[x] == 0)
                return true; 
            else if (arr[x] < 0)
                continue; 

            if (x + arr[x] < N && arr[x + arr[x]] >= 0) {
                q.push(x + arr[x]); 
            }
            if (x - arr[x] >= 0 && arr[x - arr[x]] >= 0) {
                q.push(x - arr[x]); 
            }
            arr[x] = -1; 

        }
        return false; 
    }
};