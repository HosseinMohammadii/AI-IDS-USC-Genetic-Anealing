public class Graph {
    public String path = "";
    public int[] ans;
    public int[] f;
    int barg;

    public Graph(int[] ans , int[] f) {
        this.ans = ans;
        this.f = f;
        barg = 0;
    }

    public Graph(int[] ans) {
        this.ans = ans;
        barg = 0;
    }

    public boolean ids (int[] f ,int maxDepth){
        int[] temp;
        boolean flag = true ;
        int t;
        int t1;
        for (int p = 0; p < 6 && flag; p++) {
            t1 = 4*p;
            t = f[t1];
            for(int j = 1 ; j <= 3 && flag ; j++) {
                if (f[t1 + j] != t) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag){
            System.out.println("found");
            for(int i = 0 ; i < 24 ; i++){
                System.out.print(f[i] + " , ");
            }
            System.out.println(" ");
            return true;
        }

        if (maxDepth <= 0){
//            System.out.print("0");
            barg++;
            return false;
        }

//        if(maxDepth < 3){
//            for(int i = 0 ; i < 24 ; i++){
//                System.out.print(f[i] + " , ");
//            }
//        }
//        System.out.println(" ");

        temp = f;
        temp = move(1, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "1,1 + ";
            return true;
        }

        temp = move(1, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "1,-1 + ";
            return true;
        }

        temp = move(2, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "2,1 + ";
            return true;
        }

        temp = move(2, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "2,-1 + ";
            return true;
        }
        temp = move(3, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "3,1 + ";
            return true;
        }
        temp = move(3, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "3,-1 + ";
            return true;
        }
        temp = move(4, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "4,1 + ";
            return true;
        }

        temp = move(4, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "4,-1 + ";
            return true;
        }

        temp = move(5, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "5,1 + ";
            return true;
        }

        temp = move(5, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "5,-1 + ";
            return true;
        }

        temp = move(6, 1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "6,1 + ";
            return true;
        }

        temp = move(6, -1 , f );
        if( ids(temp, (maxDepth - 1)) ){
            path = path + "6,-1 + ";
            return true;
        }

        return false;

    }

    public boolean ids2 (int maxDepth){

        boolean flag = true ;
        int t;
        int t1;
        for (int p = 0; p < 6 && flag; p++) {
            t1 = 4*p;
            t = f[t1];
            for(int j = 1 ; j <= 3 && flag ; j++) {
                if (f[t1 + j] != t) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag){
            System.out.println("found");
            for(int i = 0 ; i < 24 ; i++){
                System.out.print(f[i] + " , ");
            }
            System.out.println(" ");
            return true;
        }

        if (maxDepth <= 0){
//            System.out.print("0");
            barg++;
            return false;
        }

//        if(maxDepth < 3){
//            for(int i = 0 ; i < 24 ; i++){
//                System.out.print(f[i] + " , ");
//            }
//        }
//        System.out.println(" ");


        move2(1, 1 );
        if( ids2((maxDepth - 1)) ){
            path = path + "1,1 + ";
            return true;
        }
        move2(1, -1 );

        move2(1, -1);
        if( ids2((maxDepth - 1)) ){
            path = path + "1,-1 + ";
            return true;
        }
        move2(1, 1 );

        move2(2, 1 );
        if( ids2((maxDepth - 1)) ){
            path = path + "2,1 + ";
            return true;
        }
        move2(2, -1 );

        move2(2, -1 );
        if( ids2((maxDepth - 1)) ){
            path = path + "2,-1 + ";
            return true;
        }
        move2(2, 1 );

        move2(3, 1 );
        if( ids2((maxDepth - 1)) ){
            path = path + "3,1 + ";
            return true;
        }
        move2(3, -1 );

        move2(3, -1);
        if( ids2((maxDepth - 1)) ){
            path = path + "3,-1 + ";
            return true;
        }
        move2(3, 1 );

//        temp = move(4, 1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "4,1 + ";
//            return true;
//        }
//
//        temp = move(4, -1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "4,-1 + ";
//            return true;
//        }
//
//        temp = move(5, 1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "5,1 + ";
//            return true;
//        }
//
//        temp = move(5, -1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "5,-1 + ";
//            return true;
//        }
//
//        temp = move(6, 1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "6,1 + ";
//            return true;
//        }
//
//        temp = move(6, -1 , f );
//        if( ids2((maxDepth - 1)) ){
//            path = path + "6,-1 + ";
//            return true;
//        }

        return false;

    }


    public int[] move(int side, int direction, int[] ff) {
        int[] f = ff;
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


    public void move2(int side, int direction) {

        switch (side) {
            case 1:
                reihentausch2(0, 1, 2, 3, direction);
                reihentausch2(13, 9, 5, 23, direction);
                reihentausch2(12, 8, 4, 22, direction);
                break;
            case 2:
                reihentausch2(4, 5, 6, 7, direction);
                reihentausch2(16, 20, 0, 8, direction);
                reihentausch2(19, 23, 3, 11, direction);
                break;
            case 3:
                reihentausch2(8, 9, 10, 11, direction);
                reihentausch2(12, 17, 6, 3, direction);
                reihentausch2(15, 16, 5, 2, direction);
                break;

            case 4:
                reihentausch2(12, 13, 14, 15, direction);
                reihentausch2(22, 18, 10, 2, direction);
                reihentausch2(21, 17, 9, 1, direction);
                break;
            case 5:
                reihentausch2(16, 17, 18, 19, direction);
                reihentausch2(21, 7, 11, 15, direction);
                reihentausch2(20, 6, 10, 14, direction);
                break;
            case 6:
                reihentausch2(20, 21, 22, 23, direction);
                reihentausch2(1, 4, 19, 14, direction);
                reihentausch2(0, 7, 18, 16, direction);
                break;

            default:
                throw new InternalError("unknown side " + side);
        }
//        logAction(side, direction);
    }

    protected int[] reihentausch(int a, int b, int c, int d, int direction, int[] felld) {
        int[] feld = felld;
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

    protected void reihentausch2(int a, int b, int c, int d, int direction) {

        int temp = f[a];
        switch (direction) {
            case -1:    // counter-clockwise
                f[a] = f[b];
                f[b] = f[c];
                f[c] = f[d];
                f[d] = temp;
                break;
            case 1:    // clockwise
                f[a] = f[d];
                f[d] = f[c];
                f[c] = f[b];
                f[b] = temp;
                break;
            default:
                throw new InternalError("unknown direction " + direction);
        }
    }







    public static void main(String[] args) {
        int[] ansSample = {1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6};
        int[] input = {4 ,4 ,2 ,2, 1, 3, 6, 5, 1, 1, 5,5, 6, 3 , 3, 6 , 4, 2 , 4, 2 , 3, 1 , 5,  6};
        Graph o = new Graph(ansSample);
        int[] temp;
        int[] side = {1 ,1 , 2 , 3 ,1 , 3 , 3 , 1 ,3 , 2};
        int[] rotate = {1, 1 , -1 , 1 , -1 , -1 , -1 ,1 , -1 , 1};

        int[] side2 = new int[10];
        int[] rotate2 = new int[10];

        for(int f = 9 ; f >= 0 ; f--){
            side2[9-f] = side[f];
            rotate2[9-f] = -rotate[f];
        }



//        temp =input;
        temp = ansSample ;

//        for(int u = 0 ; u < 10 ; u++) {
//            temp = o.move(side[u], rotate[u], temp);
//        }
//
//        for(int u = 0 ; u < 10 ; u++) {
//            temp = o.move(side2[u], rotate2[u], temp);
//        }

        temp = o.move(1, 1, temp);
        temp = o.move(3, -1, temp);
        temp = o.move(2, 1, temp);

        temp = o.move(2, -1, temp);
        temp = o.move(3, 1, temp);
        temp = o.move(1, -1, temp);





        for (int i = 0; i < 24; i++) {
            System.out.print(temp[i] + "  ");
        }
        System.out.println(" ");

//        for(int p = 1 ; p <=3 ; p++) {
//            for(int y = 1 ; y <= 2 ; y++ ) {
//                if(y == 2)
//                    y = -1;
//                temp = o.move(p, y, temp);
//                for (int i = 0; i < 24; i++) {
//                    System.out.print(temp[i] + "  ");
//                }
//                System.out.println(" ");
//                if(y == -1)
//                    y = 2;
//            }
//        }



    }

}
