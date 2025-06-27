class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int h = nums.length - 1;

        if(nums[l] == target)
            return l;
        if(nums[h] == target)
            return h;
            
        while(l < h){
            if(nums[l] == target)
                return l;
            if(nums[h] == target)
                return h;
            int mid = (l + h) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                l = mid + 1;
            else
                h = mid - 1;
        }

        return -1;
    }
}