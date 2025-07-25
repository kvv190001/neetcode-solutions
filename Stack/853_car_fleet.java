class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
       int n = position.length;

       Car[] cars = new Car[n];
       for(int i = 0; i < n; i++){
        cars[i] = new Car(position[i], (double)(target-position[i])/speed[i]);
       }

       Arrays.sort(cars, (a,b) -> Integer.compare(a.position, b.position));

       int fleet = 0, t = n-1;

       while(t > 0){
        if(cars[t].time < cars[t-1].time)
            fleet += 1;
        else
            cars[t-1] = cars[t];
        t -= 1;
       }

        if(t == 0)
            return fleet + 1;
        else
            return fleet;
    }

    class Car{
        int position;
        double time;
        Car(int p, double t){
            position = p;
            time = t;
        }
    }
}