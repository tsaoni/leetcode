#include <iostream> 
#include <vector> 

using namespace std; 
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int j = 0; 
        int ret = 0; 
        for (int i = 0; i < nums1.size(); i++) {
            j = (j < i) ? i: j; 
            while ((j < nums2.size()) && (nums2[j] >= nums1[i]))
                j++; 
            if ((j > i) && (nums2[j - 1] >= nums1[i]))
                ret = max(ret, j - i - 1); 
        }
        return ret; 
    }
};

int main() {
    Solution s = Solution(); 
    vector<int> nums1 = {55,30,5,4,2}; 
    vector<int> nums2 = {100,20,10,10,5}; 
    int ret = s.maxDistance(nums1, nums2); 
    cout << "ans: " << ret << endl; 
}