st = Time.now
#t = 13195
t = 600851475143
# 600 851 475 143
prime_factors = []
product = 1

for i in 2..(t/2)
  if t % i == 0
    unless prime_factors.any? {|pf| i % pf == 0}
      product *= i
      prime_factors << i
      puts "[#{Time.now - st}s] #{i} (product: #{product})"
    end
  end

  if product > t/2 then break end
end

sol = prime_factors.join(" ")
puts "#{sol} [#{Time.now-st}s]"
