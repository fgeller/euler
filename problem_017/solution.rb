$ccount = 0


def hundreds(pre)
  # one two three four five six seven eight nine
  otn = [3, 3, 5, 4, 4, 3, 5, 5, 4] # 1..9
  # ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen
  ttn = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 10..19
  # twenty thirty fourty fifty sixty seventy eighty ninety
  tns = [6, 6, 6, 5, 5, 7, 6, 6] # 20, 30, 40 .. 90

  # 
  ret = otn.inject(0){|m,o| $ccount+=1;pre+m+o} + # 1  .. 9
    ttn.inject(0){|m,o| $ccount+=1;pre+m+o} + # 10 .. 19
    tns.inject(0){|m,o| $ccount+=1;pre+m+o + otn.inject(0){|n,p| $ccount+=1;n+pre+o+p}} # 20 .. 99
end


otn = [3, 3, 5, 4, 4, 3, 5, 5, 4] # 1..9
hundred = 7
und = 3
one_thousand = 11

sum = 0
sum += hundreds(0)
otn.each {|n| $ccount+=1;sum += hundreds(n+hundred+und) + n + hundred}
 $ccount+=1
sum += one_thousand # 1000
puts $ccount
puts sum
