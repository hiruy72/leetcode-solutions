class Solution {
public:
    // Expand around center helper: returns length of palindrome centered at (l, r)
    int expandAroundCenter(const string &s, int l, int r) {
        int n = s.size();
        while (l >= 0 && r < n && s[l] == s[r]) {
            --l;
            ++r;
        }
        return r - l - 1; // length of palindrome
    }

    string longestPalindrome(string s) {
        int n = s.size();
        if (n <= 1) return s;

        int start = 0, maxLen = 1;
        for (int i = 0; i < n; ++i) {
            // odd length (center at i)
            int len1 = expandAroundCenter(s, i, i);
            // even length (center between i and i+1)
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                // compute start index from center i and len
                start = i - (len - 1) / 2;
            }
        }
        return s.substr(start, maxLen);
    }
};
