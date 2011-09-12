st = Time.now

square_of_sum = (101 * 50) ** 2
sum_of_squares = (1..100).map {|i| i**2}.inject(0) {|m,o| m + o}

puts "#{square_of_sum - sum_of_squares} [#{Time.now-st}s]"
