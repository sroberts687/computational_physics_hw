import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Diver to test the Lagrange and CubicSplinePoly classes.
 * Generates and prints to a csv file the lagrangian polynomial and cubic
 * spline interpolation generated from a data set evaluated at 50 points.
 * Requires Lagrange and CubicSplinePoly classes.
 * 
 * MASC 340 SP15 3/3/15
 * @author Adam Anthony
 * @author AA: Revised for A06 3/25/15 
 */
public class A06Driver
{
	public static void main(String[] args) throws IOException
	{
		// Scanner
		Scanner kb = new Scanner(System.in);
		// define interval
		double a = 0.9, b = 13.3;
		// Number of times to estimate the function
		final int xIntervals = 50;

		// Define the lagrange/cubic helpers and nodes
		HashMap<Double, Double> nodes = new HashMap<>();
		Lagrange l;
		CubicSplinePoly cubic = null;

		BufferedWriter bw;

		// Open file
		while (true)
		{
			try
			{
				System.out
						.println("Enter a location to store the data ( U:\\data.csv):");
				String in = kb.nextLine();
				// If the string is empty exit the program
				if (in.equals(""))
				{
					System.out.println("Terminating program");
					return;

				}
				// Try and open file
				bw = new BufferedWriter(new FileWriter(in));

				// bw = new BufferedWriter(new FileWriter(
				// "U:\\Numerical Analysis\\Assignment 5\\data.csv"));
			} catch (Exception e)
			{
				System.out.println(e.getMessage());
				continue;
			}

			break;
		}

		// populate the nodes
		nodes.put(.9, 1.3);
		nodes.put(1.3, 1.5);
		nodes.put(1.9, 1.85);
		nodes.put(2.1, 2.1);
		nodes.put(2.6, 2.6);
		nodes.put(3.0, 2.7);
		nodes.put(3.9, 2.4);
		nodes.put(4.4, 2.15);
		nodes.put(4.7, 2.05);
		nodes.put(5.0, 2.1);
		nodes.put(6.0, 2.25);
		nodes.put(7.0, 2.3);
		nodes.put(8.0, 2.25);
		nodes.put(9.2, 1.95);
		nodes.put(10.5, 1.4);
		nodes.put(11.3, .9);
		nodes.put(11.6, .7);
		nodes.put(12.0, .6);
		nodes.put(12.6, .5);
		nodes.put(13.0, .4);
		nodes.put(13.3, .25);
		
		//Create Lagrange and interpolant 
		l = new Lagrange(nodes);
		try
		{
			cubic = new CubicSplinePoly(nodes);
		} catch (Exception e)
		{
			e.printStackTrace();
		}

		// Print header for interpolants
		bw.append("x,y,y");
		bw.newLine();

		// Loop through all xPoints.
		double dx = (b - a) / xIntervals;
		for (int x = 0; x <= xIntervals; x++)
		{
			double currX = a + x * dx;

			// add the current x value
			bw.append(Double.toString(currX));

			// output lagrangian interpolation and cubic spline interpolation
			double px = l.evaluate(currX);
			bw.append("," + px);
			px = cubic.evaluate(currX);
			bw.append("," + px);
			bw.newLine();
		}

		bw.close();
		
		//Print out table
		System.out.println("Table");
		cubic.print();
		
		
		System.out.println("File Complete");
		kb.close();
	}
}
