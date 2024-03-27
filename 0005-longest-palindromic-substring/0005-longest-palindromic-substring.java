class Solution {
    
    public String longestPalindrome(String s) {
        int strLength = s.length();

        if (strLength < 2) {
            return s;
        }

        int resultLength = 0;
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            int left = i, right = i;
            while (
                left >= 0 &&
                right < s.length() &&
                s.charAt(left) == s.charAt(right)
            ) {
                if ((right - left + 1) > resultLength) {
                    result = s.substring(left, right + 1);
                    resultLength = right - left + 1;
                }
                left -= 1;
                right += 1;
            }

            left = i;
            right = i + 1;
            while (
                left >= 0 &&
                right < s.length() &&
                s.charAt(left) == s.charAt(right)
            ) {
                if ((right - left + 1) > resultLength) {
                    result = s.substring(left, right + 1);
                    resultLength = right - left + 1;
                }
                left -= 1;
                right += 1;
            }
        }

        return result;
    }
}