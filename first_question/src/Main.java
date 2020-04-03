import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static final int        orange = 1;
    public static final int        blue = 4;
    public static final int        yellow = 6;
    public static final int        white = 3;
    public static final int        red = 5;
    public static final int        green = 2;


    int rubic[][] = new int[6][4];
    public static int[] fld = new int[24];
    private static int[] ans = {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6};
//    private LinkedList<State> stack= new LinkedList<>();
    private String path;


    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        for(int i = 0 ; i < 24 ; i++){
            int input = s.nextInt();
            System.out.print(input);
            fld[i]=input;
        }
        System.out.println(" ");
        Graph g = new Graph(ans, fld);

        int maxDepth = 0;

        while(true){
            if(g.ids2(maxDepth)){
                break;
            }
            else{
                maxDepth++;
                System.out.println("Max Depth is " + maxDepth);
            }
        }
//        System.out.println("nooow");
//        g.ids(fld,4);
//        g.ids2(10);
        System.out.println(g.barg);
        System.out.println(g.path);

    }


//    private void logAction(int side, int direction) {
//        actionLog.append(',');
//        actionLog.append(names[side]);
//        if (direction >= 0)
//            actionLog.append('+');
//        actionLog.append(direction);
//    }






}

