/*
 * PROJECT 3
 * #########
 * File: FrequencyAnalyzerMinimal.java
 * Author: Vlad Burca
 * Date: 12/08/2010
 */

import java.io.*;

public class FrequencyAnalyzerMinimal extends TextAnalyzerMinimal {
    
    protected void calcFreqs(String text, double freqs[]) {
      int l = text.length();
      int count = 0;
      String aux = new String("");
      aux = text.toLowerCase();
      double fr[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
      for (int i = 0; i < l; i++)
        if (aux.charAt(i) >= 'a' && aux.charAt(i) <= 'z') {
          fr[aux.charAt(i) - 'a'] = fr[aux.charAt(i) - 'a'] + 1;
          count = count + 1;
      }
      for (int i = 0; i < 26; i++)
        freqs[i] = fr[i] / count;
    }
    
    public String analyze(String text) {
      double chiSqr;
      chiSqr = applyChiSquare(text);
      String out = new String();
      out = "The Chi square value for this text is " + chiSqr + "\n";
      if (chiSqr > 0.25)
        out = out + "The text is PROBABLY NOT written in English.";
      else if (chiSqr >= 0.15)
        out = out + "The text is PROBABLY written in English.";
      else if (chiSqr >= 0.01)
        out = out + "The text is VERY LIKELY to be written in English.";
      else out = out + "The text is CERTAINLY written in English.";
      return out;
    }

    public static void main(String args[]) {
      if (args.length == 0) {
        System.out.println("Usage: java FrequencyAnalyzer filename");
        System.exit(0); 
      } else {
        new FrequencyAnalyzerMinimal(args[0]); 
      }
    }
    
    public FrequencyAnalyzerMinimal(String fileName) {
      System.out.println(analyze(readFile(fileName)));
    }
} // FrequencyAnalyzer

