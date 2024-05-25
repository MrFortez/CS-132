class Trick2 {
    public Trick2() {
        int counter = 0;
        while (counter > 10);
        counter++;
        System.out.println(counter + counter + "");
    }
    }
    class Trick3 {
        public Trick3(boolean run) {
            if (run) {
            int counter = 1;
            while (counter > 10)
                counter++;
            float number = 10 / counter;
            System.out.println((int)number + "");
            }
        }
    
    public String toString() {
        return "0";
        }
    }

    class Trick4 extends Trick3 {
        public Trick4() {
            super(false);
        }

        public String tostring() {
            return "1";
        }

        public void toString(int x) {
            x = 2;
            System.out.println(x);
            return;
        }

        public String ToString() {
            return "3";
        }

        public void Tostring() {
            System.out.println("4");
            return;
        }
    }

    class Trick5 {
        public Trick5() {
            // float value holding average grade per student
            int count = 5;
            // adds a value of 1 to count
            count += 2;
            // calls the barr fuction
            //count *= foo();
            count++; //; /**= foo();*/
            count /* *= ba/*r*/ *= baz(); //foo();
            // this code doesn't work for some reason
            float num = (float)(int)(float)(count + 0.5f);
            // displays the first frame in Halo 5: Guardians
            System.out.println("" + (int)count + (int)num);
        }
        
        private int bar() {
            return 3;
        }
        private int foo() {
            return 4;
        }
        private int baz() {
            return 5;
        }
    }

    public class Tricky {
        public static void main(String[] args) {
            System.out.print("Trick2: ");
            Trick2 t2 = new Trick2();
            System.out.print("Trick3: ");
            Trick3 t3 = new Trick3(true);
            System.out.print("Trick4: ");
            Trick4 t4 = new Trick4();
            System.out.println(t4);
            System.out.print("Trick5: ");
            Trick5 t5 = new Trick5();
        }
    }