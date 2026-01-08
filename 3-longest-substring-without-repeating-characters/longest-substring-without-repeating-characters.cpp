class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> window;
        int left = 0, right = 0, maxLength = 0;
        
        while (right < s.size()) {
            if (window.find(s[right]) == window.end()) {
                // character not in the set, expand window
                window.insert(s[right]);
                maxLength = max(maxLength, right - left + 1);
                right++;
            } else {
                window.erase(s[left]);
                left++;
            }
        }
        
        return maxLength;
    }
};
