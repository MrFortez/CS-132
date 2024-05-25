

public class Main {
    public static void main(String[] args) {
      System.out.println("Hello World");
      System.out.println("poggers");

      for (int i = 0; i < args.length; i++) {
        System.out.println(args[i]);
      }

    //   Fraction fraction = new Fraction(4, 20);
    //   System.out.println(fraction);
    //   System.out.println(fraction.toString());

    //   Fraction f3 = new Fraction(3,4);

    //   f3 = fraction.add(f3);
    //   System.out.println(f3);

    int[] test = {1, 2, 3};
    for (int item : test) {
        item += 1;
    }

    for (int item : test) {
        System.err.println(item);
    }


    }
  }

class Fraction {

    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator) {
        setNumerator(numerator);
        setDenominator(denominator);
        reduce();
    }

    public Fraction() {
        setNumerator(0);
        setDenominator(1);
    }

    public int getNumerator() {
        return numerator;
    }

    public int getDenominator() {
        return denominator;
    }

    public void setNumerator(int value) {
        numerator = value;
        reduce();
    }

    public void setDenominator(int value) {
        if (value != 0) {
            denominator = value;
            reduce();
        }
        else if (denominator == 0) {
            denominator = 1;
        }
    }

    private void reduce() {
        int gcd = 1;
        int min = Math.min(Math.abs(numerator),Math.abs(denominator));

        for(int i = 2; i<=min; i++)
            if (numerator % i == 0 && denominator % i == 0 ){
                gcd = i;    
            }

        numerator = numerator / gcd;
        denominator /= gcd;

        if (numerator==0){
            denominator = 1;
        }
    }

    //float - a value represented in memory with 32 bits
    //        uses IEEE 754 to represent the value
    //double - a value reprsented in memory with 64 bits
    //        uses IEEE 754 to represent the value
    private double getReal(){
        //casting is done using parentheses (type)
        //all literal decimals in java are doubles
        //float value = 6.789;
        return (double) numerator / denominator;

    }

    public Fraction add(Fraction other){
        Fraction sum = new Fraction();
        sum.numerator = numerator * other.denominator + denominator * other.numerator;
        sum.denominator = denominator * other.denominator;
        sum.reduce();
        return sum;
    }
    //use toString() to similar to __str__ in python
    public String toString(){
        return numerator + "/" + denominator + " (" + getReal() + ")";
    }

}
