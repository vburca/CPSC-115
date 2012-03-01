/*
 File: FrequencyAnalyzer.java
 Author: Vlad Burca
	 Xiaoqi Ma
 Lab Section: Wednesday

 Created:       12/01/2010
 Last Modified: 12/01/2010
*/

import java.io.*;

public class FrequencyAnalyzer {

    private FrequencyRecord[] frequencies;
    private String text;
	
	public FrequencyAnalyzer(String filename) {
	/* Constructor.
	*/
		text = readFile(filename);
		frequencies = countLetters(text);

	}

	public String getText() {
	/* Returns the text.
	*/
		return text;
	}

	public void setText(String s) {
	/* Sets the text to a specific string value.
	*/
		this.text = s;
	}

	/**
     * Reads the named text file and returns its contents as a string.
     * @param fName is a string giving the files name (full path)
     * @return the contents of fName as a String
     */
    public String readFile(String fName) {
		String msg="";
		try {
	    	File theFile = new File(fName);
	    	InputStreamReader iStream = new InputStreamReader(new FileInputStream(theFile));
	    	int length = (int)theFile.length();
	    	char input[] = new char[length];
	    	iStream.read(input);
	    	msg = new String(input);
		} catch (IOException e) {
	    	e.printStackTrace();
		} // catch
		return msg;
    }

	public FrequencyRecord[] countLetters(String s) {
	/* Counts each appearance of a letter in the string s.
	*/
		int l = (int)s.length();
		s = s.toLowerCase();
		FrequencyRecord[] freqs = new FrequencyRecord[26];
		for (char i = 'a'; i <= 'z'; i++)
		    freqs[(int)(i - 'a')] = new FrequencyRecord(i);
		for (int k = 0; k < l; k++)
			if (s.charAt(k) >= 'a' && s.charAt(k) <= 'z')
				freqs[s.charAt(k) - 'a'].setCount(freqs[s.charAt(k) - 'a'].getCount() + 1);
		return freqs;
	}

	public String toString() {
	/* Transforms the object into a string.
	*/
		String s = "";
		if (frequencies == null)
			return "No frequencies yet.";
		for (int k = 0; k < frequencies.length; k++)
			s = s + frequencies[k] + "\n";
		return s;
	}

	public void sort(FrequencyRecord[] fr) {
	/* Sorts the object by the counts of each letter.
	*/
		FrequencyRecord aux;
		for (int i = 0; i < 26; i++)
			for (int j = i + 1; j < 26; j++)
				if (fr[i].getCount() < fr[j].getCount()) {
					aux = new FrequencyRecord(fr[i].getLetter());
					aux.setCount(fr[i].getCount());
					fr[i] = fr[j];
					fr[j] = aux;
				}
	}

	public static void main(String args[]) {
		String msg="";
		FrequencyAnalyzer analyzer = new FrequencyAnalyzer(args[0]);
		if (args.length == 0) {
		    System.out.println("Usage: java FrequencyAnalyzer filename");
		    System.exit(0);
		} else {
//	    	msg = analyzer.readFile(args[0]);  // Getting the text.	
//	    	System.out.println(msg);	// Printing the text.
			System.out.println(" Unsorted frequencies: ");
			System.out.println(analyzer);
			analyzer.sort(analyzer.frequencies);
			System.out.println(" Sorted frequencies: ");
			System.out.println(analyzer);
		}	
    }

}
