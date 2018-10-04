import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * Class used to store calculate and store a cubic spline interpolation.
 * 
 * Requires Range, MapUtil, and TridiagonalMatrix classes
 * 
 * MASC 340 SP15 3/22/15
 * 
 * @author Adam Anthony
 */
public class CubicSplinePoly
{
	// key = {x[j] to x[j+1]} value = {a,b,c,d}
	private HashMap<Range, double[]> cubicSplines;

	public CubicSplinePoly(Map<Double, Double> nodes) throws Exception
	{
		// initialize cubicSplines
		cubicSplines = new HashMap<>(nodes.size() - 1);

		// Sort nodes and split into lists for direct access
		nodes = (LinkedHashMap<Double, Double>) MapUtil.sortByKey(nodes);
		ArrayList<Double> x = new ArrayList<>(nodes.keySet());
		ArrayList<Double> fx = new ArrayList<>(nodes.values());

		// Temp lists to store info on splines
		ArrayList<Range> ranges = new ArrayList<>(nodes.size() - 1);
		ArrayList<double[]> polys = new ArrayList<>(nodes.size() - 1);

		// Calculate all the ranges and add to cubicSplines along with all a's.
		while (x.size() > 0)
		{
			if (x.size() == 1)
				ranges.add(new Range(x.get(0), x.get(0)));
			else
				ranges.add(new Range(x.get(0), x.get(1)));
			
			polys.add(new double[] { fx.get(0), 0, 0, 0 });
			x.remove(0);
			fx.remove(0);
		}

		// clean up x and fx
		x = null;
		fx = null;

		// Setup tridiagonal matrix using ranges and function values and solve
		double[] c = new double[ranges.size()];
		double[] soln = new double[ranges.size()];
		double[] u = new double[ranges.size() - 1];
		double[] l = new double[ranges.size() - 1];

		// boundry conditions
		c[0] = 1;
		u[0] = 0;
		for (int i = 1; i < c.length - 1; i++)
		{
			double h = ranges.get(i).magnitude();
			double prevH = ranges.get(i - 1).magnitude();

			// setup the three diagonals
			c[i] = 2 * (prevH + h);
			u[i] = h;
			l[i - 1] = prevH;

			// setup the y as in Dx = y
			soln[i] = 3.0 / h * (polys.get(i + 1)[0] - polys.get(i)[0]) - 3.0
					/ prevH * (polys.get(i)[0] - polys.get(i - 1)[0]);
		}
		c[c.length - 1] = 1;
		l[l.length - 1] = 0;
		soln[soln.length - 1] = 0;

		c = new TridiagonalMatrix(u, c, l).solve(soln);

		// clean up arrays
		soln = null;
		u = null;
		l = null;

		// Calc and add all b's and d's to Map. Also add c's
		for (int i = 0; i < ranges.size() - 1; i++)
		{
			double h = ranges.get(i).magnitude();
			// b
			polys.get(i)[1] = (polys.get(i + 1)[0] - polys.get(i)[0]) / h - h
					/ 3.0 * (2 * c[i] + c[i + 1]);
			// c
			polys.get(i)[2] = c[i];
			
			// d
			polys.get(i)[3] = (c[i + 1] - c[i]) / (3.0 * h);

			// System.out.println(Arrays.toString(polys.get(i)));
		}

		// Add everything to the splines map
		for (int i = 0; i < ranges.size() - 1; i++)
		{
			cubicSplines.put(ranges.get(i), polys.get(i));
		}
	}

	public double evaluate(double x)
	{
		for (Entry<Range, double[]> entry : cubicSplines.entrySet())
 		{
			if (entry.getKey().contains(x))
			{
				return entry.getValue()[0] + entry.getValue()[1]
						* (x - entry.getKey().getMin()) + entry.getValue()[2]
						* (x - entry.getKey().getMin())* (x - entry.getKey().getMin()) + entry.getValue()[3]
						* (x - entry.getKey().getMin())* (x - entry.getKey().getMin())* (x - entry.getKey().getMin());
			}
		}

		return Double.NaN;
	}

	public void print()
	{
		System.out.println("x,a,b,c,d");
		for (Map.Entry<Range, double[]> entry : cubicSplines.entrySet())
		{
			System.out.println(entry.getKey().getMin() + ","
					+ entry.getValue()[0] + "," + entry.getValue()[1] + ","
					+ entry.getValue()[2] + "," + entry.getValue()[3]);
		}
	}

	public static void main(String[] args) throws Exception
	{
		HashMap<Double, Double> nodes = new HashMap<>();

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

		CubicSplinePoly poly = new CubicSplinePoly(nodes);

		poly.evaluate(0);
	}
}
