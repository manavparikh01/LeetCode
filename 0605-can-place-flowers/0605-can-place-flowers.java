class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0)
        {
            return true;
        }
        if (flowerbed.length == 0)
        {
            return false;
        }
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.length-1 || flowerbed[i+1] == 0)) {
                flowerbed[i] = 1;
                i++;
                n--;
                if (n == 0) {
                    return true;
                }
            }
        }
        return false;
//         if (n == 0)
//         {
//             return true;
//         }
//         if (flowerbed.length == 0)
//         {
//             return false;
//         }
//         int i = 0;
//         int l = flowerbed.length;
//         if (flowerbed[0] == 1)
//         {
//             i = i+2;
//         }
//         if (flowerbed[0] == 0 && flowerbed[1] == 0)
//         {
//             flowerbed[0] = 1;
//             i = i+2;
//             n = n-1;
//         }
//         while (i < flowerbed.length -1 && n != 0)
//         {
//             if (flowerbed[i] == 1)
//             {
                
//                     i = i+2;
                
//             }
//             else
//             {   
//                     if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0)
//                     {
//                         flowerbed[i] = 1;
//                         n = n-1;
//                     i = i+2;
//                     }
//             }
//         }
//         if (i == i-1)
//         {
//             if (flowerbed[i] == 0 && flowerbed[i-1] == 0)
//             {
//                 n = n-1;
//             }
//         }
//         if (n == 0)
//         {
//             return true;
//         }
//         return false; 
        }
}