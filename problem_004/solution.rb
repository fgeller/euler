st = Time.now

three_digits = (100..999).to_a.reverse

max = 0

three_digits.each do |td1|
  three_digits.each do |td2|
    product = td1 * td2
    if product.to_s == product.to_s.reverse
      max = product if product > max
    end
  end
end

sol = max
puts "[#{Time.now - st}s] #{sol}"
