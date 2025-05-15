class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> dictAnagram = new HashMap<>();


        for(String s : strs){
            int[] temp_arr = new int[26];
            for(char c : s.toCharArray()){
                temp_arr[c - 'a'] += 1;
            }
            String key = Arrays.toString(temp_arr);
            dictAnagram.put(key, dictAnagram.getOrDefault(key,new ArrayList<>()));
            dictAnagram.get(key).add(s);
        }
        
        return new ArrayList<>(dictAnagram.values());
    }
}
