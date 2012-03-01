/*
 File: Animal.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       11/17/2010
 Last Modified: 11/17/2010
*/

public class Animal {

    private String name;
    private String type;
    private String breed;
    private char gender;
    private float height;
    private float weight;
    private int age;

    public Animal() {
    }

    public Animal(String n, String t, String b, char g, float h, float w, int a) {
	name = n;
	type = t;
	breed = b;
	gender = g;
	height = h;
	weight = w;
	age = a;
    }

    public String getName() {
	return name;
    }

    public void setName(String name) {
	this.name = name;
    }

    public String getType() {
	return type;
    }
    public void setType(String type) {
	this.type = type;
    }
    public String getBreed() {
	return breed;
    }
    public void setBreed(String breed) {
	this.breed = breed;
    }

    public char getGender() {
	return gender;
    }
    public void setGender(char gender) {
	this.gender = gender;
    }

    public float  getHeight() {
	return height;
    }
    public void setHeight(float height) {
	this.height = height;
    }

    public float  getWeight() {
	return weight;
    }
    public void setWeight(float weight) {
	this.weight = weight;
    }

    public int  getAge() {
	return age;
    }
    public void setAge(int age) {
	this.age = age;
    }

    public String toString() {
	return type + " [" + name + "," + breed + "," + gender + "," + height + ","  + weight + "," + age + "]";
    }

    public void chase(Animal other) {
	System.out.println(this + " is chasing " + other);
    }

	public boolean isSameType(Animal another) {
		if (type.equals(another.type))
			return true;
		else
			return false;
	}


/*
    public static void main(String Args[]) {
	Dog collie = new Dog("Collie", 'F', 2, 50, 2);
	System.out.println(collie);
	Dog greatDane = new Dog("Great Dane", 'M', 4, 100, 5);
	System.out.println(greatDane);
	Cat tabby = new Cat("Tabby", 'F', 2, 50, 2);
	System.out.println(tabby);
	Cat calico = new Cat("Calico", 'M', 4, 100, 5);
	System.out.println(calico);
    }
*/
	public static void main(String Args[]) {
		Animal a1 = new Animal("Ami", "dog", "doggie", 'M', 12, 32, 1);
		Animal a2 = new Animal("Geae", "dogi", "minnie", 'F', 23, 12, 2);
		System.out.println(a1.isSameType(a2));
	}
}
