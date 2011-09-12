st = Time.now


def s

  for i in 1..332 do    
    for j in (i+1)..(1000-(2*i)) do     
      for k in (j+1)..(1000-(i+j))        
        if i + j + k == 1000        
          return [i, j, k] if i**2 + j**2 == k**2
        end     
      end
    end
  end

end

triplet = s()

puts "#{triplet.join("*")}=#{triplet.inject(1){|m,o| m*=o}} [#{Time.now - st}s]"
