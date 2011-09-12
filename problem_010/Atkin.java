import java.util.*;
import java.math.*;

public class Atkin {

    final static long UPPER = 10000000;
   


    static void extract_prime(TreeMap<Long, Boolean> lon, Collection<Long> lop) {
	long current_prime = lon.firstKey();

	lop.add(current_prime);
	lon.remove(current_prime);

	for (long i = current_prime*current_prime; i < UPPER; i += 2*current_prime)
	    lon.remove(i);
	

    }


    public static void main(String[] args) {

	long st = System.currentTimeMillis();

	TreeMap<Long, Boolean> nums = new TreeMap<Long, Boolean>();
	for (long i = 7; i < UPPER; i+=2)
	    if (i % 3 != 0 && i % 5 != 0 && i % 7 != 0 && i % 11 != 0)
		nums.put(i, true);	

	Collection<Long> primes = new ArrayList<Long>();
	primes.add(new Long(2));
	primes.add(new Long(3)); 
	primes.add(new Long(5)); 
	primes.add(new Long(7));
	primes.add(new Long(11));  

	while(!nums.isEmpty()) 
	    extract_prime(nums, primes);
	
	long sum = 0;
	for (long p : primes)
	    sum += p;

	System.out.println("[" + sum + " " + (System.currentTimeMillis() - st) + "ms]");
    }

}