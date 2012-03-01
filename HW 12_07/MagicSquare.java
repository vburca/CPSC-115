/*
  File: MagicSquare.java
  Author: Vlad Burca

  Created:  12/07/10
  Modified: 12/07/10
*/


import java.io.*;
import java.util.*;

public class MagicSquare {

  private int n;     // the size of a square
  private int M[][]; // an array reference for a square

  public MagicSquare() {
  }

  public void readSquare() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    System.out.print("Enter the size of your square: ");
    st = new StringTokenizer(br.readLine()) ;
    n = Integer.parseInt(st.nextToken());
    System.out.println();
    M = new int[n][n];
    System.out.println("Now, enter a square by rows.");
    System.out.println();
    for (int i = 0; i < n; i++) {
      System.out.print("Enter row " + i + ": ");
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++)
        M[i][j] = Integer.parseInt(st.nextToken());
    }
  }
  
  public void tabPrint(int k) {
    int space = 0;
    String tab = "";
    if (k < 10) space = 3;
    if (k >=10 && k < 100) space = 2;
    if (k >=100 && k < 1000) space = 1;
    for(int i = 0; i < space; i++)
      tab = tab + " ";
    System.out.print(tab + k);
  }
  
  public void printSquare() {
    System.out.println("The square you entered");
    System.out.println();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++)
        tabPrint(M[i][j]);
      System.out.println();
    }
  }

  private int checkSums(int Sum[], int size) {
    for (int i = 0; i < size-1; i++)
      if (Sum[i] != Sum[i+1])
        return -1;
    return Sum[0];
  }
  
  public int checkRows() {
    int sumR[] = new int[n];
    for (int i = 0; i < n; i++) {
      sumR[i] = 0;
      for (int j = 0; j < n; j++)
        sumR[i] = sumR[i] + M[i][j];
    }
    return checkSums(sumR, n);
  }
  
  public int checkColumns() {
    int sumC[] = new int[n];
    for (int j = 0; j < n; j++) {
      sumC[j] = 0;
      for (int i = 0; i < n; i++)
        sumC[j] = sumC[j] + M[i][j];
    }
    return checkSums(sumC, n);
  }
  
  public int checkDiagonals(){
    int sumD[] = new int[2];
    sumD[0] = 0;
    sumD[1] = 0;
    for (int i = 0; i < n; i++) {
      sumD[0] = sumD[0] + M[i][i];
      sumD[1] = sumD[1] + M[i][(n-1)-i];
    }
    return checkSums(sumD, 2);   
  }
  
  public boolean areDistinct() {
    int check[] = new int[n*n + 1];
    for (int i = 1; i <= n*n; i++)
      check[i] = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) {
        if (M[i][j] < 1 || M[i][j] > n*n)
          return false;
        if (check[M[i][j]] == 1)
          return false;
        else
          check[M[i][j]] = check[M[i][j]] + 1;
    } 
    return true;
  }
  
  public boolean isMagic() {
    if (areDistinct() && checkRows() == checkColumns() && checkColumns() == checkDiagonals())
      return true;
    else
      return false;    
  }
  
  public static void main(String args[]) throws IOException {

    MagicSquare MS = new MagicSquare();
    MS.readSquare();
    System.out.println();
    MS.printSquare();
    System.out.println();
    // check Functions:
/* 
    System.out.print("checkRows(): ");
    System.out.print(MS.checkRows());
    System.out.println();
    System.out.print("checkColumns(): ");
    System.out.print(MS.checkColumns());
    System.out.println();
    System.out.print("checkDiagonals(): ");
    System.out.print(MS.checkDiagonals());
    System.out.println();
*/
    // distinct Function:
/*
    System.out.print("areDistinct(): ");
    System.out.print(MS.areDistinct());
*/
    if (MS.isMagic())
      System.out.println("is a magic square!");
    else
      System.out.println("is not a magic square!");
  }

}