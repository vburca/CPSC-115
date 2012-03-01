/*
 File: Dog.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       11/17/2010
 Last Modified: 11/17/2010
*/

public class Dog extends Animal {

    public Dog() {
    }

    public Dog(String n, String b, char g, float h, float w, int a) {
        super(n, "Dog", b, g, h, w, a);      // Invoke the Animal constructor
    }
/*
    public static void main(String args[]){
	Dog collie = new Dog("Collie", 'F', 2, 50, 2);
	System.out.println(collie);
	Dog greatDane = new Dog("Great Dane", 'M', 4, 100, 5);
	System.out.println(greatDane);
    }
*/
}
