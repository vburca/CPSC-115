/*
 File: Cat.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       11/17/2010
 Last Modified: 11/17/2010
*/

public class Cat extends Animal {

    public Cat() {
    }

    public Cat(String n, String b, char g, float h, float w, int a) {
        super(n, "Cat", b, g, h,w,a);      // Invoke the Animal constructor
    }
/*
    public static void main(String args[]){
	Cat tabby = new Cat("Tabby", 'F', 2, 50, 2);
	System.out.println(tabby);
	Cat calico = new Cat("Calico", 'M', 4, 100, 5);
	System.out.println(calico);
    }
*/
}
