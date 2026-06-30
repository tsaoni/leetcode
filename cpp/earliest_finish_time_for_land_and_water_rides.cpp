#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        int ret = 4001, lf = 4001, wf = 4001; 
        int n = landStartTime.size(), m = waterStartTime.size(); 
        for (int i = 0; i < n; i++)
            lf = min(lf, landStartTime[i] + landDuration[i]); 
        for (int i = 0; i < m; i++)
            wf = min(wf, waterStartTime[i] + waterDuration[i]); 
        for (int i = 0; i < m; i++)
            ret = min(ret, (lf > waterStartTime[i]) ? lf + waterDuration[i]: waterStartTime[i] + waterDuration[i]); 
        for (int i = 0; i < n; i++)
            ret = min(ret, (wf > landStartTime[i]) ? wf + landDuration[i]: landStartTime[i] + landDuration[i]); 
        return ret; 
            
    }
};