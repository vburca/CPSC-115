/*
 File: PublicMethods.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       11/17/2010
 Last Modified: 11/17/2010
*/

public class PublicMethods {

    public static void main(String Args[]) {
	Dog collie = new Dog("Collie", 'F', 2, 50, 2);
	Cat tabby = new Cat("Tabby", 'M', 1, 40, 3);
	System.out.println(" I am a " + collie.getBreed() + " and I am " + collie.getGender());
	System.out.println(" I am a " + tabby.getBreed() + " and I am " + tabby.getGender());

	System.out.println();
	System.out.println(collie);
	collie.setAge(collie.getAge() + 1);
	System.out.println(collie);
    }

}
