class Solution {
    static int n;
    static int arr[][];
    static int dp[];

    static int search(int st, int end, int x){
        int ans = -1;
        while(st<=end){
            int mid = st+(end-st)/2;

            if(arr[mid][0]>=x){
                ans = mid;
                end = mid-1;
            }else st = mid+1;
        }
        return ans;
    }

    static int helper(int idx){
        if(idx>=n) return 0;
        if(dp[idx]!=-1) return dp[idx];

        int a = helper(idx+1);
        int next = search(idx+1,n-1,arr[idx][1]);
        int b = arr[idx][2];
        if(next!=-1){
            b = arr[idx][2]+helper(next);
        }
        return dp[idx] = Math.max(a,b);
    }
    public int jobScheduling(int[] st, int[] end, int[] p) {
        n = st.length;
        arr = new int[n][3];
        for(int i=0; i<n; i++){
            arr[i] = new int[]{st[i],end[i],p[i]};
        }
        Arrays.sort(arr,(a,b)->(a[0]-b[0]));
        dp = new int[50005];
        Arrays.fill(dp,-1);
        return helper(0);
    }
    
    
    
    
    
    
//     HashMap<Integer, Integer> hm;
    
//     public class startend
//     {
//         int start;
//         int end;
//         int profit;
        
//         startend(int start, int end, int profit)
//         {
//             this.start = start;
//             this.end = end;
//             this.profit = profit;
//         }
//     }
    
//     public class ComparatorStartend implements Comparator<startend>
//     {
//         @Override
//         public int compare(startend s1, startend s2)
//         {
//             if (s1.start <= s2.start)
//             {
//                 return -1;
//             }
//             return 1;
//         }
//     }
    
//     public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
//         //assuming that startime is sorted
//         if (startTime.length == 1)
//         {
//             return profit[0];
//         }
//         ArrayList<startend> se = new ArrayList<startend>();
//         for (int i = 0; i< startTime.length;i++)
//         {
//             se.add(new startend(startTime[i], endTime[i], profit[i]));
//         }
//         ComparatorStartend cs = new ComparatorStartend();
//         Collections.sort(se, cs);
//         hm = new HashMap<Integer, Integer>();
//         ArrayList<Integer> all = new ArrayList<Integer>();
//         for(int i = 0;i<se.size();i++)
//         {
//             all.add(dp(se, i));
//         }
//         Collections.sort(all, Collections.reverseOrder());
        
//         return all.get(0);
//     }
    
//     public int dp(ArrayList<startend> se, int i)
//     {
//         if (hm.containsKey(i) == true)
//         {
//             return hm.get(i);
//         }
//         if (i == se.size() - 1)
//         {
//             hm.put(i, se.get(i).profit);
//             return se.get(i).profit;
//         }
//         int res = dp(se, i+1);
//         // ArrayList<Integer> al = new ArrayList<Integer>();
//         // al.add(se.get(i).profit);
//         int j = bs(se, se.get(i).end, i+1, se.size()-1);
//         // for(int j = i+1;j<se.size();j++)
//         // {
//         //     if (se.get(j).start < se.get(i).end)
//         //     {
//         //         continue;
//         //     }
//         //al.add(dp(se, j));
//         // }
//         //Collections.sort(al, Collections.reverseOrder());
//         // if (al.size() == 0)
//         // {
//         //     hm.put(i, se.get(i).profit);
//         //     return se.get(i).profit;
//         // }
//         int ansss = 0;
//         if (j != -1)
//         {
//             ansss = dp(se, j) + se.get(i).profit;
//         }
//         int anss = Math.max(res, ansss);
//         hm.put(i, anss);
//         return anss;
//     }
    
//     private int bs(ArrayList<startend> se, int end, int left, int right) {
//         int ans = -1;
//         while(left<=right){
//             int mid = left+(right-left)/2;

//             if(se.get(mid).start>=end){
//                 ans = mid;
//                 right = mid-1;
//             }else left = mid+1;
//         }
//         return ans;
//     }
}