class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int minK = 1;
        int maxK = piles[0];
        int n = piles.length;

        for(int i = 1; i < n; i++){
            if(maxK < piles[i])
                maxK = piles[i];
        }

        int k;
        int result  = maxK;

        while(minK <= maxK){
            k = (minK + maxK)/2;

            long count = 0;
            for(int i = 0; i < n; i++){
                if(piles[i] < k)
                    count += 1;
                else if(piles[i] % k == 0)
                    count += piles[i]/k;
                else
                    count += piles[i]/k + 1;
            }

            if(count <= h){
                result = k;
                maxK = k - 1;
            }
            else
                minK = k + 1;
        }

        return result;
    }
}