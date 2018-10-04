import java.util.*;

/**
 * Group of utility function for Java Maps.
 * 
 * @author Adam Anthony (3/25/2015)
 * @author Dan Ciborowski (7/24/2014)
 * @author Carter Page (4/3/2012)
 *
 */
public class MapUtil
{
	/**
	 * Returns a linked hash map representation of the original map
	 * sorted by key
	 * 
	 * Based on code from http://stackoverflow.com/posts/2581754/revisions
	 * 
	 * @return sortedMap
	 * @author Adam Anthony (3/25/2015)
	 * @author Dan Ciborowski (7/24/2014)
	 * @author Carter Page (4/3/2012)
	 *
	 */
	public static <K extends Comparable<? super K>, V > Map<K, V> sortByKey(
			Map<K, V> map)
	{
		List<Map.Entry<K, V>> list = new LinkedList<>(map.entrySet());

		Collections.sort(list, new Comparator<Map.Entry<K, V>>() 
				{
			@Override
			public int compare(Map.Entry<K, V> o1, Map.Entry<K, V> o2)
			{
				return (o1.getKey()).compareTo(o2.getKey());
			}
		});

		Map<K, V> result = new LinkedHashMap<>();
		for (Map.Entry<K, V> entry : list)
		{
			result.put(entry.getKey(), entry.getValue());
		}
		return result;
	}

}
