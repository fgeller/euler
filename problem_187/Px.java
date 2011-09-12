import java.util.*;
import java.math.*;

public class Px {

       
    private int limit;
    private int sqrt_limit;
    
    public Px(Integer limit) {
        this.limit = limit;
        this.sqrt_limit = (new Double(Math.sqrt(limit))).intValue();
    }

    public int[] sieve() {

        boolean[] is_prime = new boolean[this.limit+1];

        for (int x = 1; x <= this.sqrt_limit; x++) {
            for (int y = 1; y <= this.sqrt_limit; y++) {
                int n;

                n = 4*x*x + y*y;
                if (n <= this.limit && (n % 12 == 1 || n % 12 == 5))
                    is_prime[n] = !is_prime[n];
                
                n = 3*x*x + y*y;
                if (n <= this.limit && n % 12 == 7)
                    is_prime[n] = !is_prime[n];
                
                n = 3*x*x - y*y;
                if (x > y && n <= limit && n % 12 == 11)
                    is_prime[n] = !is_prime[n];         
            }
        }

	int[] sums_primes = new int[this.limit+1];
	int current = 0;
	//haxor
	is_prime[2] = true;
	is_prime[3] = true;
	is_prime[5] = true;
        for (int n = 1; n <= this.limit; n++) {
            if (is_prime[n]) {
                if (n <= this.sqrt_limit) {
                    for (int i = n*n; i >= 0 && i <= this.limit; i += n*n)
                        is_prime[i] = false;
                }
		current += 1;
                //primes.add(n);
            }
	    sums_primes[n] = current;
	}

        return sums_primes;
    }

    public static void main(String[] args) {
	int l = Integer.parseInt(args[0]);
        Px px = new Px(l);
        
	int[] primes_summed = px.sieve();
	List<Integer> primes = new ArrayList<Integer>();
	int prev = primes_summed[0];
	for (int i = 1; i < primes_summed.length; i++) {
	    if (primes_summed[i] > prev)
		primes.add(i);

	    prev = primes_summed[i];
	}

	System.out.println("total of " + primes.size() + " primes below " + l);

	int sqrt_l = (new Double(Math.sqrt(l))).intValue();

	int low = primes.get(0);
	int up = 0;
	for (int i = 0; i < primes.size(); i++) {
	    if (primes.get(i) > sqrt_l)
		break;
	    up = primes.get(i);
	}

	System.out.println("low:" + low + " up:" + up);


	int stupid = 0;
	for (int p : primes) {
	    if (p > sqrt_l)
		break;
	    //System.out.println("l/p["+(l/p)+"]:" + primes_summed[l/p]);
	    //System.out.println("p-1["+(p-1)+"]:" + primes_summed[p-1]);
	    stupid += primes_summed[l/p] - primes_summed[p-1];
	    //System.out.println("accum: "+ stupid);
	    
	}

	System.out.println("accum: " + stupid);
    }

}