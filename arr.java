public class arr {
    public static void main(String[] args){
        int arr[] = {1,4,5,6,7};

        System.out.println(binsch(arr, 5));
    }
    private static int binsch(int[] number ,int find){
        int low = 0;

        int high = number.length -1 ;

        while (low <= high){

            int middle = (low + high ) / 2;
            int mid = number[middle];
            
            if (find == mid){
                return middle ;
            }
            if (find <= mid){
                high = middle - 1; // case left
            }
            else {
                low = middle + 1 ; // case right 
            }
        }
        return - 1;
    }
}