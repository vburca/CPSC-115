public class FrequencyRecord {
    private char letter;
    private int count;

    public FrequencyRecord(char ch) {
	this.letter = ch;
	this.count = 0;
    }

    public char getLetter() { return letter; }
    public void setLetter(char ch) { letter = ch; }
    public int getCount() { return count; }
    public void setCount(int n) { count = n; }

    public String toString() {
	return "" + letter + ": " + count;
    }

    public static void main(String args[]) {
	FrequencyRecord r1 = new FrequencyRecord('a');  // Record for letter 'a'
	System.out.println(r1);                         // Print the record
	r1.setCount(1);                                 // Set its count to 1
	System.out.println(r1);                         // Print it again
    }

}