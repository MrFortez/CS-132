


class ShapeTest {
    
    public static void main(String[] args) {

        Rectangle rect = new Rectangle(4, 3);
        rect.draw();

        Square square = new Square(6);
        square.draw();

        Triangle tri = new Triangle(5);
        tri.draw();

    }
}


abstract class Shape {

    // Instance Variables
    protected int length;
    protected int width;

    public Shape() {
        length = 1;
        width = 1;
    }

    public Shape(int length, int width) {
        this.length = length;
        this.width = width;
    }

    public void draw() {
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < length; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }

}

class Rectangle extends Shape {

    public Rectangle(int length, int width) {
        super(length, width);
    }
}

class Square extends Rectangle {

    public Square(int side) {
        super(side, side);
    }
}

class Triangle extends Shape {

    public Triangle(int side) {
        super(side, side);
    }

    public void draw() {
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < length - i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
}