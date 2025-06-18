class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> sDict = new HashMap<>();

        int n = s.length();
        int m = t.length();

        if(n != m){
            return false;
        }

        for(int i = 0; i < n; i++){
            char c = s.charAt(i);
            sDict.put(c, sDict.getOrDefault(c, 0) + 1);
        }

        for(int i = 0; i < m; i++){
            char c = t.charAt(i);
            sDict.put(c, sDict.getOrDefault(c, 0) - 1);
            if(sDict.get(c) < 0){
                return false;
            }
        }

        return true;
    }
}