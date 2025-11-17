class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int lastOneIndex = -1; // stores index of the previous 1

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                if (lastOneIndex != -1 && i - lastOneIndex - 1 < k) {
                    return false; // distance between 1s is less than k
                }
                lastOneIndex = i; // update last 1 index
            }
        }

        return true; // all 1s are at least k apart
    }
};
