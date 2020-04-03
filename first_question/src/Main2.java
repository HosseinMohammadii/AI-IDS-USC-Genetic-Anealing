import java.util.LinkedList;
import java.util.Scanner;

public class Main2 {

    public static final int        orange = 1;
    public static final int        blue = 4;
    public static final int        yellow = 6;
    public static final int        white = 3;
    public static final int        red = 5;
    public static final int        green = 2;


    int rubic[][] = new int[6][4];
    public static int[] fld = new int[24];
    private static int[] ans = {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6};
    private static LinkedList<State> pq = new LinkedList<>();
    private String path;


    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        for(int i = 0 ; i < 24 ; i++){
            int input = s.nextInt();
            System.out.print(input);
            fld[i]=input;
        }
        System.out.println(" ");





        State root = new State(fld,"",0);
        pq.addLast(root);
        State temp;
        State temp2;
        State goal = new State(fld,"",0);
        int[] temp3;
        boolean flag = true ;
        boolean flag2 = true ;
        int t;
        int t1;
        while(flag){

            temp = pq.getFirst();
            pq.removeFirst();

            for (int p = 0; p < 6 && flag2; p++) {
                t1 = 4*p;
                t = temp.field[t1];
                for(int j = 1 ; j <= 3 && flag2 ; j++) {
                    if (temp.field[t1 + j] != t) {
                        flag2 = false;
                        break;
                    }
                }
            }
            if (flag2){
                System.out.println("found");
                for(int i = 0 ; i < 24 ; i++){
                    System.out.print(temp.field[i] + " , ");
                }
                System.out.println(" ");
                goal = temp;
                break;
            }

            for(int p = 1 ; p <=3 ; p++) {
                for(int y = 1 ; y <= 2 ; y++ ) {
                    if(y == 2){
                        y = -1;
                    }

                    temp3 = move(p, y, temp.field);
                    temp2 = new State(temp3,temp.path+(p+","+y+"+"),temp.depth+1);
//                    System.out.println(temp.depth);
                    pq.addLast(temp2);

                    if(y == -1){
                        y = 3;
                    }
                }
            }



        }

//        System.out.println(barg);
        System.out.println(goal.path);

    }


    public static int[] move(int side, int direction, int[] fff) {
        int[] f = new int[24];
        for(int i = 0 ; i < 24 ; i++){
            f[i] = fff[i];
        }

        switch (side) {
            case 1:
                f = reihentausch(0, 1, 2, 3, direction, f);
                f = reihentausch(13, 9, 5, 23, direction, f);
                f = reihentausch(12, 8, 4, 22, direction, f);
                break;
            case 2:
                f = reihentausch(4, 5, 6, 7, direction, f);
                f = reihentausch(16, 20, 0, 8, direction, f);
                f = reihentausch(19, 23, 3, 11, direction, f);
                break;
            case 3:
                f = reihentausch(8, 9, 10, 11, direction, f);
                f = reihentausch(12, 17, 6, 3, direction, f);
                f = reihentausch(15, 16, 5, 2, direction, f);
                break;

            case 4:
                f = reihentausch(12, 13, 14, 15, direction, f);
                f = reihentausch(22, 18, 10, 2, direction, f);
                f = reihentausch(21, 17, 9, 1, direction, f);
                break;
            case 5:
                f = reihentausch(16, 17, 18, 19, direction, f);
                f = reihentausch(21, 7, 11, 15, direction, f);
                f = reihentausch(20, 6, 10, 14, direction, f);
                break;
            case 6:
                f = reihentausch(20, 21, 22, 23, direction, f);
                f = reihentausch(1, 4, 19, 14, direction, f);
                f = reihentausch(0, 7, 18, 16, direction, f);
                break;

            default:
                throw new InternalError("unknown side " + side);
        }
//        logAction(side, direction);
        return f;
    }

    protected static int[] reihentausch(int a, int b, int c, int d, int direction, int[] ft) {
        int[] feld = new int[24];
        for(int i = 0 ; i < 24 ; i++){
            feld[i] = ft[i];
        }

        int temp = feld[a];
        switch (direction) {
            case -1:    // counter-clockwise
                feld[a] = feld[b];
                feld[b] = feld[c];
                feld[c] = feld[d];
                feld[d] = temp;
                break;
            case 1:    // clockwise
                feld[a] = feld[d];
                feld[d] = feld[c];
                feld[c] = feld[b];
                feld[b] = temp;
                break;
            default:
                throw new InternalError("unknown direction " + direction);
        }
        return feld;
    }


}
