class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> pMap = new HashMap<>();
        
        pMap.put(')', '(');
        pMap.put(']', '[');
        pMap.put('}', '{');

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(pMap.containsValue(c))
                stack.push(c);
            else{
                if(stack.isEmpty() || stack.pop() != pMap.get(c))
                    return false;
            }
        }

        if(stack.size() > 0)
            return false;
        return true;
    }
}