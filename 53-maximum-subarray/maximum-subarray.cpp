class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int maxEndingHere = nums[0]; // max sum ending at current position
        int maxSoFar = nums[0];      // max sum overall
        
        for (int i = 1; i < nums.size(); ++i) {
            // either extend current subarray or start new subarray
            maxEndingHere = max(nums[i], maxEndingHere + nums[i]);
            maxSoFar = max(maxSoFar, maxEndingHere);
        }
        
        return maxSoFar;
    }
};
