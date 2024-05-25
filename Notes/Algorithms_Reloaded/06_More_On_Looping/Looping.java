
class WhileLoops {
    public static void main(String[] args) {
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }

        int j = 0;
        do {
            System.out.println(j);
        } while (i < 5);
    }
}

class ForLoops{

    public static void main(String[] args) {
        for (int k = 0; k < 10; k++) {
            System.out.println(k);
        }

        for (int i = 0, j = 0; i < 10 && j < 5; i++, j += 2) {
            System.out.println(i + j);
        }

        double[] values = {3.14, 2.72, 1.62, 6.28, 9.81};
        for (double val : values) {
            System.out.println(val);
        }
    }
}
