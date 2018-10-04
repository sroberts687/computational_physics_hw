/**
 * Stores a numeric range. MASC 340 SP15 3/22/15
 * 
 * @author Adam Anthony
 */
public class Range
{
	private double min = Double.NEGATIVE_INFINITY,
			max = Double.POSITIVE_INFINITY;

	public Range() throws Exception
	{
		this(0, 0);
	}

	public Range(double min, double max) throws Exception
	{
		setMin(min);
		setMax(max);
	}

	public boolean contains(double x)
	{
		return (x >= min) && (x <= max);
	}

	public double magnitude()
	{
		return Math.abs(max - min);
	}

	public double getMin()
	{
		return min;
	}

	public void setMin(double min) throws Exception
	{
		if (min > max) throw new Exception(min + "isn't <= " + max);
		this.min = min;
	}

	public double getMax()
	{
		return max;
	}

	public void setMax(double max) throws Exception
	{
		if (min > max)
			throw new Exception("Min must be less than or equal to max");
		this.max = max;
	}

	@Override
	public String toString()
	{
		return "{" + min +", "+ max +"}";
			}
}
