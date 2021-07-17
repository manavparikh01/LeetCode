class Solution {
    public int[] plusOne(int[] digits) {
        int rem = 1;        
        for(int i = digits.length-1; i>=0; i--){
            int incr = digits[i]+rem;
            rem =0;
            digits[i] = incr;
            if(incr>9){
                digits[i] = incr%10;
                rem = incr/10;
            }
        }
        if(rem !=0){
            int[] result = new int[digits.length+1];
            System.arraycopy(digits,0,result,1,digits.length);
            result[0] = rem;
            return result;
        }
        return digits;
    }
}