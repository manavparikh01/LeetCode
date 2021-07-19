class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int length = candies.length;
        int max = 0;
        ArrayList<Boolean> list = new ArrayList<Boolean>();
        for (int i=0;i<length;i++)
        {
            if (candies[i] > max)
            {
                max=candies[i];
            }
        }
        for (int i=0;i<length;i++)
        {
            if (candies[i]+extraCandies>=max)
            {
                list.add(true);
            }
            else {
                list.add(false);
            }
        }
        return list;
    }
}