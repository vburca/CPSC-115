/*
 * PROJECT 3
 * #########
 * File: TextAnalyzer.java
 * Author: Vlad Burca
 * Date: 12/08/2010
 */

import java.io.*;

public abstract class TextAnalyzer {

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
    
    protected final double frenchFrequency[] = { 
      0.083,                               // a
      0.008, 0.033, 0.039, 0.171,          // b,c,d,e
      0.009, 0.011, 0.005, 0.071,          // f,g,h,i
      0.002, 0.001, 0.060, 0.022,          // j,k,l,m
      0.082, 0.055, 0.029, 0.013,          // n,o,p,q
      0.073, 0.081, 0.062, 0.062,          // r,s,t,u
      0.018, 0.001, 0.005, 0.003, 0.001};  // v,w,x,y,z
    
    protected final double italianFrequency[] = { 
      0.118,                               // a
      0.007, 0.047, 0.029, 0.119,          // b,c,d,e
      0.012, 0.022, 0.021, 0.109,          // f,g,h,i
      0.001, 0.001, 0.063, 0.033,          // j,k,l,m
      0.056, 0.088, 0.031, 0.009,          // n,o,p,q
      0.065, 0.046, 0.058, 0.040,          // r,s,t,u
      0.022, 0.001, 0.001, 0.001, 0.004};  // v,w,x,y,z
    
    protected final double spanishFrequency[] = { 
      0.099,                               // a
      0.014, 0.044, 0.053, 0.141,          // b,c,d,e
      0.008, 0.009, 0.007, 0.071,          // f,g,h,i 
      0.004, 0.001, 0.050, 0.033,          // j,k,l,m
      0.069, 0.094, 0.032, 0.014,          // n,o,p,q
      0.065, 0.073, 0.047, 0.041,          // r,s,t,u
      0.008, 0.001, 0.004, 0.016, 0.003};  // v,w,x,y,z
    
    protected final double[] languageFrequency[] = {null, englishFrequency, frenchFrequency, 
      italianFrequency, spanishFrequency};
    
    
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
    
    protected double applyChiSquare(int n, String text) {
      double chiSqr = 0;
      double freqs[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
      calcFreqs(text, freqs);
      chiSqr = chiSquare(languageFrequency[n], freqs);
      return chiSqr;
    }
    
    protected double chiSquare(double exp[], double obs[]) {
      double chiS = 0;
      for (int i = 0; i < 26; i++)
        chiS = chiS + (obs[i] - exp[i])*(obs[i] - exp[i])/exp[i];
      return chiS;
    }
    
    protected abstract void calcFreqs(String text, double freqs[]);
    
    public abstract String analyze(int n, String text);

} // TextAnalyzer

