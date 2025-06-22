class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int h = height.length - 1;
        int maxWater = 0;

        while(l < h){
            maxWater = Math.max(maxWater, (h-l)*Math.min(height[l],height[h]));
            if(height[l] < height[h])
                l += 1;
            else
                h -= 1;
        }

        return maxWater;
    }
}