class Solution {
    
    class painter
    {
        int cost;
        int time;
        double val;
        
        painter(int cost, int time, double val)
        {
            this.cost = cost;
            this.time = time;
            this.val = val;
        }
    }
    
    class ComparatorPainter implements Comparator<painter> {
        @Override
            public int compare(painter p1, painter p2)
            {
                if (p1.val < p2.val)
                {
                    return -1;
                }
                else if (p1.val > p2.val)
                {
                    return 1;
                }
                else if (p1.cost > p2.cost)
                {
                    return 1;
                }
                else if (p1.val == p2.val)
                {
                    if (p1.cost > p2.cost)
                    {
                        return 1;
                    }
                    else return -1;
                }
                return 1;
            }
        
    }
    
    public int solve(int[] cost,int[] time,int curr,int wallRemain,int[][] dp){
        if(wallRemain <= 0){
            return 0;
        }
        if(curr >= cost.length){
            return 2000000000;
        }
        if(dp[curr][wallRemain] != -1){
            return dp[curr][wallRemain];
        }
        int Paint = cost[curr] + solve(cost,time,curr+1,wallRemain - time[curr] - 1,dp);
        int noPaint = solve(cost,time,curr+1,wallRemain,dp);

        return dp[curr][wallRemain] = Math.min(Paint,noPaint);
    }
    
    public int paintWalls(int[] cost, int[] time) {
        int[][] dp = new int[501][501];
        for(int i=0; i<cost.length+1; i++){
            Arrays.fill(dp[i],-1);
        }
        return solve(cost,time,0,cost.length,dp); 
        
        
        
        
        
        
        
        
        
        
        // ArrayList<painter> al = new ArrayList<painter>();
        // for(int i = 0; i<cost.length;i++)
        // {
        //     al.add(new painter(cost[i], time[i], (double)(cost[i]/time[i])));
        // }
        // ComparatorPainter cp = new ComparatorPainter();
        // Collections.sort(al, cp);
        // for(int i = 0; i<cost.length;i++)
        // {
        //     System.out.println(al.get(i).cost + " " + al.get(i).val);
        // }
        // int l = 0;
        // int r = cost.length;
        // int costn = 0;
        // while (l < r)
        // {
        //     costn += al.get(l).cost;
        //     int fn = al.get(l).time;
        //     while (fn > 0 && l<r)
        //     {
        //         fn -= 1;
        //         r -= 1;
        //     }
        //     System.out.println(costn + " " + l + " " + r + " " + al.get(l).cost);
        //     l += 1;
        //     //System.out.println(costn + " " + l + " " + r + " " + al.get(l).cost);
        // }
        //return 56;
    }
}