public class Dog {

    private String breed;
    private char gender;
    private float height;
    private float weight;
    private int age;

    public Dog() {
    }

    public Dog(String b, char g, float h, float w, int a) {
	breed = b;
	gender = g;
	height = h;
	weight = w;
	age = a;
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
	return "Dog: [" + breed + "," + gender + "," + height + ","  + weight + "," + age + "]";
    }
    
    public static void main(String args[]){
	Dog collie = new Dog("Collie", 'F', 2, 50, 2);
	System.out.println(collie);
	Dog greatDane = new Dog("Great Dane", 'M', 4, 100, 5);
	System.out.println(greatDane);
    }
}
