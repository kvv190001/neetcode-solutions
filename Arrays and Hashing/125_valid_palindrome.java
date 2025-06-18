class Solution {
    public boolean isPalindrome(String s) {
        String newS = "";

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isLetterOrDigit(c))
                newS += Character.toLowerCase(c);
        }
        System.out.println(newS);
        int n = newS.length();
        for(int i = 0; i < n / 2; i++){
            if(newS.charAt(i) != newS.charAt(n - i - 1))
                return false;
        }

        return true;
    }
}