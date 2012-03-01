/*
 File: TestAnimals.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       11/17/2010
 Last Modified: 11/17/2010
*/

public class TestAnimals {

    public static void main(String Args[]) {
	Dog collie = new Dog("Fido", "Collie", 'F', 2, 50, 2);
	System.out.println(collie);
	Dog greatDane = new Dog("Big guy", "Great Dane", 'M', 4, 100, 5);
	System.out.println(greatDane);
	Cat tabby = new Cat("Rocky", "Tabby", 'F', 2, 50, 2);
	System.out.println(tabby);
	Cat calico = new Cat("Blummy", "Calico", 'M', 4, 100, 5);
	System.out.println(calico);
	Cow cow1 = new Cow("Jeff", "Cow", 'M', 4, 100, 6);
	System.out.println(cow1);
	System.out.println();
	collie.chase(greatDane);
    }

}
