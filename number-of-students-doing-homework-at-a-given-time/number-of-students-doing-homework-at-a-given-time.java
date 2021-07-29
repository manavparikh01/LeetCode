class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int num = 0;
        for (int i=0;i<startTime.length;i++)
        {
            if (startTime[i] <= queryTime && queryTime <=endTime[i])
            {
                num+=1;
            }
        }
        return num;
    }
}