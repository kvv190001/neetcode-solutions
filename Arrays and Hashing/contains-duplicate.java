import java.util.HashMap;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dictInt = new HashMap<>();

        int n = nums.length;

        for(int i = 0; i < n; i++){
            dictInt.put(nums[i], dictInt.getOrDefault(nums[i], 0) + 1);
            if(dictInt.get(nums[i]) > 1){
                return true;
            }
        }

        return false;
    }
}
