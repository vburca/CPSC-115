public class RandomTester {

    private int[] numbers;    // An array of random inegers

  	  /**
  	   * Constructor creates an int array of random integers between 1..n
  	   * @param n is the size of the array and the upper bound of random integers.
  	   */
    public RandomTester(int n) {
		numbers = new int[n];
		for (int k = 0; k < numbers.length; k++) {
			numbers[k] = 1 + (int)(Math.random() * n);
		}
    }

	/* 
		Printing the array of numbers.
	*/
	public void print() {
		int n = numbers.length;
		for (int i = 0; i < n; i++)
			System.out.print(numbers[i] + " ");
		System.out.println();
	}

	/* 
		Sorting the array of numbers.
	*/
	public void sort() {
		int n = numbers.length;
		int v;
		int j;
		for (int i = 0; i < n; i++) {
			v = numbers[i];
			j = 0;
			for (j = i-1; j >= 0; j--) {
				if (numbers[j] <= v)
					break;
				numbers[j+1] = numbers[j];
			}
			numbers[j+1] = v;
		}
	}

	/*
		Finds the median of the array of numbers.
	*/
	public double findMedian() {
		int n = numbers.length;
		if (n % 2 != 0)
			return numbers[n/2];
		else 
			return (double)((numbers[n/2 - 1] + numbers[n/2])) / 2.0;
	}

   	 /**
  	  * Main takes an optional command line argument to set the size of 
   	  *  array of random integers. If no command line argument is provided
   	  *  n is set to 10 by default. 
   	  * Usage:  java RandomTester [n]
   	  */

    public static void main(String args[]) {
		int n = 10;
		if (args.length > 0) 
		    n = Integer.parseInt(args[0]);
		RandomTester random = new RandomTester(n);
		long t1 = System.currentTimeMillis();
//		System.out.println("Random array: ");
//		random.print();
		random.sort();
//		System.out.println("Sorted array: ");
//		random.print();
		long t2 = System.currentTimeMillis();		

//		Median
		double median = random.findMedian();
		System.out.println("Median: " + median);

//		Deviation
		double deviation;
		deviation = Math.abs((median - n / 2.0) / n);
		System.out.println("Deviation = " + deviation);

//		Testing Speed
		double time = (t2 - t1) / 1000.0;
		System.out.println("Time = " + time + " seconds.");
    }
   

}
