class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int n = temperatures.length;
        int[] answer = new int[n];

        for(int i = 0; i < n; i++){
            while(!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                int index = stack.pop();
                answer[index] = i - index;
            }
            stack.push(i);
        }

        return answer;
    }
}