st = Time.now

primes = [2]
n = 3
until primes.size == 10001
  n += 2
  primes << n unless primes.any? {|p| n % p == 0}
end


puts "#{primes.last} [#{Time.now-st}s]"
