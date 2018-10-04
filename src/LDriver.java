/**
 * LDiver to test the Lagrange class.
 * Generates and prints to a csv file the 5 lagrange interpolate curves, and Lagrangian 
 * polynomials for two functions f(x) and g(x), and the associated absolute error.
 * 
 * Calculates the Lagrangian polynomial using both equispaced nodes and Chebyshev nodes.
 * AA: Fix of Chebyshev nodes and file selection 3/17/15
 * 
 * @author Adam Anthony
 * MASC 340 SP15 3/3/15
 * 
 */
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class LDriver
{
	public static void main(String[] args) throws IOException
	{
		// Scanner
		Scanner kb = new Scanner(System.in);
		// define interval
		double a = -1, b = 1;
		// define number of nodes-1
		int n = 4;
		// NUmber of times to estimate the function
		final int xIntervals = 50;
		
		//Define the lagrange helpers
		Lagrange lF = new Lagrange();
		Lagrange lG = new Lagrange();
		Lagrange lGChebsy = new Lagrange();
		
		BufferedWriter bw;

		// Open file
		while (true)
		{
			try
			{
				System.out
						.println("Enter a location to store the data ( U:\\data.csv):");
				String in = kb.nextLine();
				//If the string is empty exit the program
				if(in.equals(""))
				{
					System.out.println("Terminating program");
					return;
					
				}
				//Try and open file
				bw = new BufferedWriter(new FileWriter(in));
				
				//bw = new BufferedWriter(new FileWriter(
				//		"U:\\Numerical Analysis\\Assignment 5\\data.csv"));
			} catch (Exception e)
			{
				System.out.println(e.getMessage());
				continue;
			}

			break;
		}

		// populate the nodes
		for (int i = 0; i <= n; i++)
		{
			double x = a + (double) i * (b - a) / n;
			double cRoot = chebyshevRoot(i + 1, n);

			lF.addNode(x, f(x));
			lG.addNode(x, g(x));
			lGChebsy.addNode(cRoot, g(cRoot));
		}

		// Print header for interpolants
		bw.append("x");
		for (int i = 0; i <= n; i++)
		{
			bw.append(",y");
		}

		bw.append(",P(x),f(x),|P(x)-f(x)|,P(x),f(x),|P(x)-f(x)|,P(x),f(x),|P(x)-f(x)|");
		bw.newLine();

		// Loop through all xPoints.
		double dx = (b - a) / xIntervals;
		for (int x = 0; x <= xIntervals; x++)
		{
			double currX = a + x * dx;

			// add the current x value
			bw.append(Double.toString(currX));

			// add all values for the Lagrangian interpolate polynomials
			for (int i = 0; i <= n; i++)
			{
				// interpolant(k, x)
				bw.append(","
						+ lF.interpolant(a + (double) i * (b - a) / n, currX));
			}

			// output P(x), f(x), and abs(p-f) to file for 3
			double px = lF.evaluate(currX);
			bw.append("," + px + "," + f(currX) + ","
					+ Math.abs(px - f(currX)));

			// output P(x), f(x), and abs(p-f) to file for 4
			px = lG.evaluate(currX);
			bw.append("," + px + "," + g(currX) + ","
					+ Math.abs(px - g(currX)));

			// output P(x), f(x), and abs(p-f) to file for 5
			px = lGChebsy.evaluate(currX);
			bw.append("," + px + "," + g(currX) + ","
					+ Math.abs(px - g(currX)));

			bw.newLine();
		}

		bw.close();
		System.out.println("File Complete");
		kb.close();
	}

	public static double f(double x)
	{
		return -3 * x * x * x + 2.5 * x * x - x + 3;
	}

	public static double g(double x)
	{
		return -0.25 * Math.exp(x) * Math.sin(3 * x);
	}

	public static double chebyshevRoot(int k, int n)
	{
		return Math.cos((2.0 * k - 1) / (2.0 * (n+1)) * Math.PI);
	}

}
