/*
 File: FrequencyRecord.java
 Author: Vlad Burca
	 Xiaoqi Ma
 Lab Section: Wednesday

 Created:       12/01/2010
 Last Modified: 12/01/2010
*/

public class FrequencyRecord {

    private char letter;
    private int count;
	
	public FrequencyRecord(char ch) {
		letter = ch;
		count = 0;
	}

	public char getLetter() {
		return letter;
	}

	public void setLetter(char ch) {
		this.letter = ch;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int n) {
		this.count = n;
	}

	public String toString() {
		return letter + ": " + count;
	}

	public static void main(String Args[]) {
		FrequencyRecord r1 = new FrequencyRecord('a');
		System.out.println(r1);
		r1.setCount(1);
		System.out.println(r1);
		System.out.println(r1.getLetter());
	}

}
