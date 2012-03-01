/*
 File: main.java
 Author: Vlad Burca
 Lab Section: Wednesday

 Created:       12/01/2010
 Last Modified: 12/01/2010
*/

public class TestMain {
	
	public static void main(String Args[]) {
		FrequencyRecord r1 = new FrequencyRecord('a');
		System.out.println(r1);
		r1.setCount(1);
		System.out.println(r1);
		System.out.println(r1.getLetter());
	}

}
