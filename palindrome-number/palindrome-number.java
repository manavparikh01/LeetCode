class Solution {
    public boolean isPalindrome(int x) {
        int temp = 0;
        int num = x;
        int y = 0;
        while (num > 0) {
            y = num%10;
            temp=temp*10 + y;
            num= num/10;
        }
        if (temp == x) {
            return true;
        } else {
            return false;
        }
    }
}