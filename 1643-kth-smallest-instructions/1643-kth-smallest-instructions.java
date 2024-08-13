class Solution {
        public String kthSmallestPath(int[] destination, int k) {
            int[][] dp = new int[destination[0]+1][destination[1]+1];
	for(int i = 0; i <= destination[0]; i++){
		for(int j = 0; j <= destination[1]; j++) {
			if(i == 0 && j == 0) dp[i][j] = 1;
			else if(i == 0) dp[i][j] = dp[i][j - 1];
			else if(j == 0) dp[i][j] = dp[i - 1][j];
			else dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
		}
	}
	StringBuilder sb = new StringBuilder();
	int i = destination[0], j = destination[1];
	while(i != 0 && j != 0) {
	    // if k is smaller than or equal with the number of paths starting with H, then we pick 'H' for current position.
		if(dp[i][j - 1] >= k) {
			j--;
			sb.append('H');
		// if k is larger than the number of paths starting with 'H', we have to pick V then.
		}else {
			k -= dp[i][j - 1];
			i--;
			sb.append('V');
		}
	}
	for(int m = 0; m < i; m++) sb.append('V');
	for(int m = 0; m < j; m++) sb.append('H');
	return sb.toString();
        }
//     public String st;
//     public int kth;
//     public String kthSmallestPath(int[] destination, int k) {
//         st = "";
        
//         String s = "";
//         int n = destination[0] + destination[1];
//         int r = destination[0];
//         double an = ncr(n, r);
//         if ((double)(k) <= (double)an/2)
//         {
//             kth = k;
//             dp(destination[0], destination[1], k, s, 0, 0);
//         }
//         else
//         {
//             kth = (int)an - k;
//             dpp(destination[0], destination[1], k, s, 0, 0);
//         }
//         return st;
//     }
    
//     public void dp(int a, int b, int k, String s, int m, int n)
//     {
//         if (kth == 0)
//         {
//             return;
//         }
//         if (m > a || n > b)
//         {
//             return;
//         }
//         if (m == a && n == b)
//         {
//             kth -= 1;
//             //System.out.println(k + " " + s);
//         }
//         if (kth == 0)
//         {
//             st = s;
//             return;
//         }
//         //horizontal
//         dp(a, b, k, s + "H", m, n+1);
//         //vertical
//         dp(a, b, k, s + "V", m+1, n);
//         return;
//     }
    
//     public void dpp(int a, int b, int k, String s, int m, int n)
//     {
//         if (kth == 0)
//         {
//             return;
//         }
//         if (m > a || n > b)
//         {
//             return;
//         }
//         if (m == a && n == b)
//         {
//             kth -= 1;
//             //System.out.println(k + " " + s);
//         }
//         if (kth == 0)
//         {
//             st = s;
//             return;
//         }
//         //horizontal
//         dpp(a, b, k, s + "V", m+1, n);
//         dpp(a, b, k, s + "H", m, n+1);
//         //vertical
        
//         return;
//     }
    
//     public double ncr(int a, int b)
//     {
//         int upp = 1;
//         for (int i = 1;i<=a;i++)
//         {
//             upp *= i;
//         }
//         int downb = 1;
//         for (int i = 1;i<=b;i++)
//         {
//             downb *= i;
//         }
//         int downab = 1;
//         for (int i = 1;i<=(a-b);i++)
//         {
//             downab *= i;
//         }
//         return (double)(upp/(double)(downab*downb));
//     }
}