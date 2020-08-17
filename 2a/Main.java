
public class Main {

    private static long startTime;
    private final static int TIMEOUT_SECONDS = 120;
    public static void main(String[] args) {
	// write your code here

        try {
            int i = 0;
            while (true) {
                startTime = System.currentTimeMillis();
                long[] result = lucasSeries(i);
                System.out.println("lucas " + i + " is " + result[0] + " - computed with " + result[1] + " call" + (result[1] > 1 ? "s" : "") + "  in " + (result[2] / 1000.0) + " seconds");
                i++;
            }
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }

    private static long[] lucasSeries(int n) throws Exception {
        assert n > 0 : "The lucas number index must be a nonnegative index";
        assert TIMEOUT_SECONDS > 0 : "The maximum amount of wall clock time must be a positive integer";

        try {
            long[] result = series(n);
            result[2] = System.currentTimeMillis() - startTime;
            return result;
        }catch(Exception ex){
            throw new Exception("Timeout at lucas " + n + " after " + TIMEOUT_SECONDS + " seconds");
        }
    }

    private static long[] series(int n) throws Exception {
       long current = System.currentTimeMillis();
       if(current - startTime > TIMEOUT_SECONDS * 1000){
           throw new Exception();
       }
        long[] result = new long[3];
        if(n == 0){
            result[0] = 2;
            result[1] = 1;
            return result;
        }else if(n == 1){
            result[0] = 1;
            result[1] = 1;
            return result;
        }else{
            long[] leftSum = series(n - 1);
            long[] rightSum = series(n - 2);

            result[0] = leftSum[0] + rightSum[0];
            result[1] = leftSum[1] + rightSum[1] +1;
            return result;
        }
    }
}
