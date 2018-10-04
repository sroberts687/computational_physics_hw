import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Class used to store a tridiagonal matrix. Can also solve the system of linear
 * equations given by Dx=C, where D is a tridiagonal matrix.
 * 
 * @author Adam Anthony MASC 340 SP15 3/22/15
 */
@SuppressWarnings("unused")
public class TridiagonalMatrix
{
	//Also used upperDiag of U matrix
	private double[] upperDiag;
	//Used as diagonal of L matrix
	private double[] midDiag;
	//Used as lower diag of L matrix
	private double[] lowerDiag;
	//flag for if matrix has been factored into LU
	private boolean factored;

	public TridiagonalMatrix(double[] upperDiag, double[] midDiag,
			double[] lowerDiag) throws Exception
	{
		// If the diagonal's sizes don't make sense throw an error
		if (upperDiag.length + 1 != midDiag.length
				|| lowerDiag.length + 1 != midDiag.length)
			throw new Exception(
					"The upper and lower diagonals much each contain "+
					"one less element than the mid diagonal.");

		this.upperDiag = upperDiag;
		this.lowerDiag = lowerDiag;
		this.midDiag = midDiag;
		this.factored = false;
	}

	public TridiagonalMatrix(Scanner file) throws Exception
	{
		this(getDiag(file), getDiag(file), getDiag(file));
	}

	private static double[] getDiag(Scanner file) throws Exception
	{
		double[] returnDiag;
		try
		{
			// Separate next line into substrings w/ ',' deliminator
			String[] diag = file.nextLine().split(",");
			returnDiag = new double[diag.length];

			// Parse all the strings into doubles and return the resulting array
			for (int i = 0; i < diag.length; i++)
			{
				returnDiag[i] = Double.parseDouble(diag[i]);
			}
		} catch (Exception e)
		{
			throw new Exception("File isn't formatted correctly");
		}

		return returnDiag;
	}

	
	public double[] solve(double[] b) throws Exception
	{
		if (b.length != midDiag.length)
			throw new Exception("b must have " + midDiag.length + " elements");
		
		// Factor into L an U
		factor();

		// Forward solve
		double[] x = new double[midDiag.length];
		
		//Boundary condition
		x[0] = b[0]/midDiag[0];
		for(int i =1; i < midDiag.length;i++)
		{
			x[i] = (b[i]-lowerDiag[i-1]*x[i-1])/midDiag[i];
		}
		
		// back solve for x
		for(int i = x.length -2; i >= 0; i--)
		{
			x[i] -= upperDiag[i]*x[i+1];
		}
		return x;
	}
	
	private void factor()
	{
		if(factored)
			return;
		//Boundary condition
		upperDiag[0] /= midDiag[0];
		for(int i =1; i < midDiag.length-1;i++)
		{
			midDiag[i] -= lowerDiag[i-1]*upperDiag[i-1];
			upperDiag[i] /= midDiag[i];
		}
		midDiag[midDiag.length-1] -= lowerDiag[midDiag.length-2]*upperDiag[midDiag.length-2];
		
		factored = true;
	}

	// Test main function
	public static void main(String[] args) throws Exception
	{
		TridiagonalMatrix matrix = new TridiagonalMatrix(new Scanner(
				new BufferedReader(new FileReader("U:\\matrix1.txt"))));
		System.out.println(Arrays.toString(matrix.solve(new double[] {-1.0,6,12,-5})));
		
		matrix = new TridiagonalMatrix(new Scanner(
				new BufferedReader(new FileReader("U:\\matrix2.txt"))));
		System.out.println(Arrays.toString(matrix.solve(new double[] {16,30,48,74,38,32,20})));
		System.out.println("aka Domino's phone number");

	}
}
