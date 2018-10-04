/**
 * Class used to calculate the Lagrangian polynomial of a set of nodes.
 * 
 * @author Adam Anthony
 * MASC 340 SP15 3/3/15
 */

import java.util.HashMap;
import java.util.Map;

public class Lagrange
{
	private HashMap<Double, Double> nodes;

	public Lagrange(HashMap<Double, Double> nodes)
	{
		this.nodes = nodes;
	}

	public Lagrange()
	{
		this(new HashMap<Double, Double>());
	}

	// add a node
	public void addNode(double x, double y)
	{
		nodes.put(x, y);
	}

	// Returns the value of the Lagrangian polynomial at x
	public double evaluate(double x)
	{
		double fx = 0;

		for (Map.Entry<Double, Double> node : nodes.entrySet())
		{
			if (node.getValue() != 0)
				fx += node.getValue() * interpolant(node.getKey(), x);
		}
		return fx;
	}

	// k is the x value at the kth index, x is the value the function should be
	// evaluated at. For most cases should be a private function.
	public double interpolant(double k, double x)
	{
		double interpolant = 1;

		for (Map.Entry<Double, Double> node : nodes.entrySet())
		{
			if (node.getKey() != k)
				interpolant *= (x - node.getKey()) / (k - node.getKey());
		}

		return interpolant;
	}

	// Test main function
	public static void main(String[] args)
	{
		// setup lagrange
		Lagrange l = new Lagrange();
		l.addNode(-1, 2);
		l.addNode(0, -1);
		l.addNode(1, 0);

		double x = 3;
		System.out.println(l.evaluate(x));
		System.out.println(2 * x * x - x - 1);
	}

}
