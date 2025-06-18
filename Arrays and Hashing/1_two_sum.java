class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dictInt = new HashMap<>();

        int n = nums.length;
        int[] arr = {0,1};

        for(int i = 0; i < n; i++){
            if(dictInt.containsKey(target - nums[i])){
                arr[0] = dictInt.get(target-nums[i]);
                arr[1] = i;
                break;
            }
            dictInt.put(nums[i], i);
        }

        return arr;
    }
}