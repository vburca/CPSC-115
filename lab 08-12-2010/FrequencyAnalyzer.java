/*
 * File: FrequencyAnalyzer.java
 * Author: Java, Java, Java
 * Description: This class analyzes a file and text to determine what
 *  language it is written in--English, French, etc.
 */

import java.io.*;

public class FrequencyAnalyzer {
    private FrequencyRecord[] frequencies;
    private String text;
    private int[][] bigrams;

    public FrequencyAnalyzer(String filename) {
	text = readFile(filename);
	frequencies = countLetters(text);
	bigrams = countBigrams(text);
    }

    public String getText() { return text; }
    public void setText (String s) { text = s; }

    public FrequencyRecord[] getFrequencies() { return frequencies; }
    public void setFrequencies(FrequencyRecord[] freqs) { frequencies = freqs; }

    public int[][]getBigrams() { return bigrams; }
    public void setBigrams(int[][] bigs) { bigrams = bigs; }

    public String getBigramTable() {
	String result = "";
	if (bigrams != null) {
	    for (int j = 0; j < bigrams.length; j++)  {
		for (int k = 0; k < bigrams[j].length; k++) {
		    result += bigrams[j][k] + " ";
		}
		result  += "\n";
	    }
	}
	return result;
    }

    public String toString() {
        String result = "";
	if (frequencies != null) {
	    for (int k = 0; k < frequencies.length; k++) {
		result += frequencies[k] + "\n";
	    }
	}
	return result;
    }

    /**
     */
    public int[][] countBigrams(String s) {
	int[][] bigs = new int[26][26];
	s = s.toLowerCase();
	for (int k = 0; k < s.length()-1; k++) {
	    char ch = s.charAt(k);
	    char ch1 = s.charAt(k+1);
	    if (ch >= 'a' && ch <= 'z' && ch1 >= 'a' && ch1 <= 'z') {
		int indx = ch  - 'a';
		int indx1 = ch1 -'a';
		bigs[indx][indx1]++;
	    }
	}
	return bigs;
    }


    /** 
     * Counts the letters in a String, s.
     * @param , the String whose letters are counted.
     * @return freqs, an array of FrequencyRecords storing the counts
     */
    public FrequencyRecord[] countLetters(String s) {
	FrequencyRecord[] freqs = new FrequencyRecord[26];
	s = s.toLowerCase();
	for (int k = 0; k < freqs.length; k++) {
	    freqs[k] = new FrequencyRecord((char)('a' + k));
	}
	for (int k = 0; k < s.length(); k++) {
	    char ch = s.charAt(k);
	    if (ch >= 'a' && ch <= 'z'){
		int indx = ch  - 'a';
		freqs[indx].setCount(freqs[indx].getCount() + 1);
	    }
	}
	return freqs;
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
	    InputStreamReader iStream = new InputStreamReader( new FileInputStream(theFile));
	    int length = (int)theFile.length();
	    char input[] = new char[length];
	    iStream.read(input);
	    msg = new String(input);
	} catch (IOException e) {
	    e.printStackTrace();
	} // catch
	return msg;
    }


	/*	
		Sorts the frequencies array by the counts of the letters.
	*/
	public void sort(FrequencyRecord[] fr) {
		int v;
		int j;
		for (int i = 0; i < 26; i++) {
			v = fr[i].getCount();
			j = 0;
			for (j = i-1; j >= 0; j--) {
				if (fr[j].getCount() >= v)
					break;
				fr[j+1].setCount(fr[j].getCount());
			}
			fr[j+1].setCount(v);
		}
	}
    
    public static void main(String args[]) {
	String msg="";
	if (args.length == 0) {
	    System.out.println("Usage: java FrequencyAnalyzer filename");
	    System.exit(0);
	} else {
	    FrequencyAnalyzer analyzer = new FrequencyAnalyzer(args[0]);
//	    System.out.println(analyzer.toString());
	    analyzer.sort(analyzer.frequencies);
	    System.out.println(analyzer.toString());

	}
    }
} // FrequencyAnalyzer

