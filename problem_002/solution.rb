def fib(n)

  if n == 1 || n == 2 then n
  else fib(n-1) + fib(n-2)
  end
  
end

#(1..10).each {|n| puts fib(n) }

#puts fib(32)

time_start = Time.now

sol = (2..32).to_a.
  select {|n| (n - 2) % 3 == 0}.
  map {|n| fib(n)}.
  select {|n| (n % 2 == 0)}.
  inject {|memo,obj| memo += obj }


time_end = Time.now


puts "#{sol} [#{time_end - time_start}s]" 

