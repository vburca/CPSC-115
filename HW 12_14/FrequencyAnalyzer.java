/*
 * PROJECT 3
 * #########
 * File: FrequencyAnalyzer.java
 * Author: Vlad Burca
 * Date: 12/08/2010
 */

import java.io.*;
import java.util.*;

public class FrequencyAnalyzer extends TextAnalyzer {
    
  protected String language[] = {null, "English", "French", "Italian", "Spanish"};
  
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
    
    public String analyze(int n, String text) {
      double chiSqr;
      chiSqr = applyChiSquare(n, text);
      String out = new String();
      out = "The Chi square value for this text is " + chiSqr + "\n";
      if (chiSqr > 0.25)
        out = out + "The text is PROBABLY NOT written in " + language[n];
      else if (chiSqr >= 0.15)
        out = out + "The text is PROBABLY written in " + language[n];
      else if (chiSqr >= 0.01)
        out = out + "The text is VERY LIKELY to be written in " + language[n];
      else out = out + "The text is CERTAINLY written in " + language[n];
      return out;
    }

    public static void main(String args[]) throws IOException {
      if (args.length == 0) {
        System.out.println("Usage: java FrequencyAnalyzer filename");
        System.exit(0); 
      } else {
        new FrequencyAnalyzer(args[0]); 
      }
    }
    
    public FrequencyAnalyzer(String fileName) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st;
      System.out.println("You may select the language you want to test your file: ");
      System.out.println("\t\t 1. English");
      System.out.println("\t\t 2. French");
      System.out.println("\t\t 3. Italian");
      System.out.println("\t\t 4. Spanish");
      System.out.print("Please choose your option: ");
      st = new StringTokenizer(br.readLine());
      int n = 0;
      n = Integer.parseInt(st.nextToken());
      while (n < 1 || n > 4) {
        System.out.println("You may select the language you want to test your file: ");
        System.out.println("\t\t 1. English");
        System.out.println("\t\t 2. French");
        System.out.println("\t\t 3. Italian");
        System.out.println("\t\t 4. Spanish");
        System.out.print("Please choose your option: ");
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
      }
      System.out.println(analyze(n, readFile(fileName)));
    }
} // FrequencyAnalyzer

