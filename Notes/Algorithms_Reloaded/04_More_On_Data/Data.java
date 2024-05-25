class Data {
    public static void main(String[] args) {
        // primative types 
        // integers:
        //  Byte (8-bit two's comp)
        //  short (16-bit two's comp)
        //  int (32-bit two's comp)
        //  long (64-bit two's comp)
        // 

        int a;
        a = 1;
        System.out.println(a);

        // floating point numbers
        // float (32 bit IEEE 754)
        // double (64 bit IEEE 754)

        double value1 = 6.78;
        // literals are doubles
        float value2 = (float) 4.57;
        float value3 = 4.543f;

        // Characters
        // 16 bit unicode characters
        // single quotes
        char notC = 'C';

        // boolean
        // 1 bit value
        boolean amIAwesome = true;



    }
    
}

class FormatSpecifiers {

    public static void main(String[] args) {
        String sentence = String.format("Hi %s, do you have %d apples?", "george", 2354);
    }
}