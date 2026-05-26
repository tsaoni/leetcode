#include <vector> 
#include <iostream> 
#include <algorithm> 

using namespace std; 
class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        vector<int> factory_flatten = {}; 
        for (int i = 0; i < factory.size(); i++) {
            for (int j = 0; j < factory[i][1]; j++)
                factory_flatten.push_back(factory[i][0]); 
        }
        sort(robot.begin(), robot.end()); 
        sort(factory_flatten.begin(), factory_flatten.end()); 
        
        int n = robot.size(), m = factory_flatten.size(); 
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, -1)); 
        for (int i = 0; i < (m + 1); i++)
            dp[0][i] = 0; 
        for(int robot_idx = 1; robot_idx < (n + 1); robot_idx++) {
            for (int factory_id = 1; factory_id < (m + 1); factory_id++) {
                
                if (dp[robot_idx - 1][factory_id - 1] >= 0) {
                    if (dp[robot_idx][factory_id] < 0)
                        dp[robot_idx][factory_id] = dp[robot_idx - 1][factory_id - 1] + static_cast<long long>(abs(robot[robot_idx - 1] - factory_flatten[factory_id - 1])); 
                    else
                        dp[robot_idx][factory_id] = min(dp[robot_idx][factory_id], 
                            dp[robot_idx - 1][factory_id - 1] + static_cast<long long>(abs(robot[robot_idx - 1] - factory_flatten[factory_id - 1]))); 
                }
                    
                if (dp[robot_idx][factory_id - 1] >= 0) {
                    if (dp[robot_idx][factory_id] < 0)
                        dp[robot_idx][factory_id] = dp[robot_idx][factory_id - 1]; 
                    else 
                        dp[robot_idx][factory_id] = min(dp[robot_idx][factory_id], dp[robot_idx][factory_id - 1]); 
                }
                    
            }
        }
        return dp[n][m]; 
    }
};

int main() {
    Solution s = Solution(); 
    // vector<int> robot = {0,4,6}; 
    // vector<vector<int>> factory = {{2,2},{6,2}}; 
    vector<int> robot = {1,-1}; 
    vector<vector<int>> factory = {{-2,1},{2,1}}; 
    int ret = s.minimumTotalDistance(robot, factory); 
    cout << "ans: " << ret << endl; 
}