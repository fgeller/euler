st = Time.now

numbers = (2..1999999).to_a
#numbers = (2..199999).to_a
primes = [2, 3, 5]



ignores = [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 50, 51, 52, 54, 55, 56, 57, 58]

puts numbers.size

numbers.reject! {|n| ignores.include?(n % 60) }

puts numbers.size

until numbers.empty?  
  primes = primes << numbers.shift
  puts primes.last
  numbers.reject {|n| n % primes.last == 0}
  puts numbers.size
end


puts "[#{primes.inject(0) {|m,o| m+o}} #{Time.now - st}s]"
