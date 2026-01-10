// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std; 

struct Task {
    long long t;
    int room_id;
    int type; 

    // For a Max-Heap, higher priority value comes first
    bool operator<(const Task& other) const {
        if (type == 0) {
            if (t != other.t) return t > other.t;
            return room_id > other.room_id;
        }
        else {
            return room_id > other.room_id;
        }
        
    }
};
class Solution {
public:
    void printQueue(priority_queue<Task> pq) {
        while (!pq.empty()) {
            Task x = pq.top(); 
            cout << x.t << " " << x.room_id << endl;
            pq.pop(); 
        }
        cout << endl;
    }
    
    void print2DVector(const std::vector<std::vector<int>>& matrix) {
        for (const auto& row : matrix) {       // Access each row
            for (int val : row) {              // Access each element in the row
                std::cout << val << " ";
            }
            std::cout << "\n";                 // New line after each row
        }
    }

    
    int mostBooked(int n, vector<vector<int>>& meetings) {
        
        vector<int> rooms(n, 0);
        priority_queue<Task> avail, unavail;
        for(int i = 0; i < n; i++){
            Task x = {0, i, 1}; 
            avail.emplace(x); 
        }
        // Task a = {0, 1}, b = {0, 0}; 
        // cout << (a < b) << endl; 
        // printQueue(pq); 
        // cout << pq << endl; 
        
        sort(meetings.begin(), meetings.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });
        // print2DVector(meetings);
        for (const auto& m: meetings) {       
            int start = m.at(0), end = m.at(1);    
            while (unavail.size() > 0 && unavail.top().t <= start) {
                Task x = unavail.top(); 
                unavail.pop(); 
                x.type = 1; 
                avail.emplace(x); 
            }
            if (avail.size() > 0) {
                Task x = avail.top(); 
                avail.pop(); 
                x.t = end; 
                x.type = 0; 
                unavail.emplace(x); 
                rooms[x.room_id]++; 
            }
            else {
                Task x = unavail.top(); 
                unavail.pop(); 
                x.t += (end - start); 
                unavail.emplace(x); 
                rooms[x.room_id]++; 
            }
            // pq.pop(); 
            // if (x.t <= start) 
            //     x.t = end; 
            // else
            //     x.t = (end - start) + x.t; 
            // rooms[x.room_id]++; 
            // pq.push(x); 
            // printQueue(pq); 
            // cout << "t" << pq.top().t << " " << pq.top().room_id << endl;
        }
        
        int ret = 0, val = 0; 
        // cout << "xxx\n"; 
        for (int i = 0; i < n; i++)
            if (val < rooms[i]) {
                val = rooms[i]; 
                ret = i; 
                // std::cout << val << " " << ret << " ";
            }
        // cout << endl; 
        // for (int val : rooms) {              // Access each element in the row
        //     std::cout << val << " ";
        // }
        // std::cout << "\n";   
        return ret; 
    }
};




int main() {
    // int n = 2; 
    // vector<vector<int>> meetings = {{0,10},{1,5},{2,7},{3,4}}; 
    int n = 3; 
    vector<vector<int>> meetings = {{1,20},{2,10},{3,5},{4,9},{6,8}}; 
    // int n = 4; 
    // std::vector<std::vector<int>> meetings = {
    //     {18, 19},
    //     {3, 12},
    //     {17, 19},
    //     {2, 13},
    //     {7, 10}
    // };
    Solution sol; 
    int ret = sol.mostBooked(n, meetings); 
    cout << ret << endl; 
    return 0;
}