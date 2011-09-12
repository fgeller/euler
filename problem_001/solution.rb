puts (1..999).to_a.select{ |n| (n % 3 == 0) || (n % 5 == 0) }.inject(0) { |memo,obj| memo += obj }
