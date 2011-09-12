st = Time.now
i = 2520
divs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#divs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while true
  i += 2520
  if divs.all? {|div| i % div == 0 }
    puts "#{i} [#{Time.now - st}s]"
  end
end
