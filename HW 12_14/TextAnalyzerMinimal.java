/*
 * PROJECT 3
 * #########
 * File: TextAnalyzerMinimal.java
 * Author: Vlad Burca
 * Date: 12/08/2010
 */

import java.io.*;

public abstract class TextAnalyzerMinimal {

    /**
     * englishFrequency array gives the relative frequencies of the characters 'a' to 'z'.
     *  For example, the letter 'e' has frequency 0.111, which means approximately 11.1% of characters in 
     *  English text are 'e'. The text used for these data was Tom Sawyer by Mark Twain.
     */
    protected final double englishFrequency[] = { 
      0.073,                                // a = 97   i.e., 73 occurences out of 1000, roughly 7.3%
      0.016, 0.019, 0.049, 0.111,           // b,c,d,e = 11.1%
      0.021, 0.017, 0.067, 0.062,           // f,g,h,i
      0.002, 0.013, 0.040, 0.032,           // j,k,l,m
      0.066, 0.091, 0.017, 0.001,           // n,o,p,q = 0.1% i.e., 1 per 1000
      0.053, 0.061, 0.099, 0.032,           // r,s,t,u
      0.009, 0.025, 0.001, 0.025, 0.0001};  // v,w,x,y,z

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
    
    protected double applyChiSquare(String text) {
      double chiSqr = 0;
      double freqs[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
      calcFreqs(text, freqs);
      chiSqr = chiSquare(englishFrequency, freqs);
      return chiSqr;
    }
    
    protected double chiSquare(double exp[], double obs[]) {
      double chiS = 0;
      for (int i = 0; i < 26; i++)
        chiS = chiS + (obs[i] - exp[i])*(obs[i] - exp[i])/exp[i];
      return chiS;
    }
    
    protected abstract void calcFreqs(String text, double freqs[]);
    
    public abstract String analyze(String text);

} // TextAnalyzer

