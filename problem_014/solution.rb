max = {}
maxp = 0
upper_limit = ARGV.shift

visited={1 => 1}

all = {}

for i in 2..(upper_limit.to_i() -1)
  count = 0
  temp = i
  
  until visited[temp]

    count += 1
    if temp % 2 == 0
    then temp /= 2
    else temp += 2*temp + 1
    end
    
  end

  count += visited[temp]
  visited[i] = count
  if count > maxp
    maxp = count
    max = {i => count}
  end
  
  #all[i] = count
end


require 'pp'
#pp all
puts
pp max

