st = Time.now

class BinaryNode
  attr_accessor :value, :left_parent, :right_parent
  def initialize(val)
    @value = val
  end
end

root = nil
rows = []

File.open("triangle.txt", "r") do |f|

  parent_line = nil
  null = BinaryNode.new(0)
  
  while (line = f.gets)        
    nodes = line.split.map {|str| BinaryNode.new(str.to_i) }

    if root.nil?
      root = nodes.first
    else
      for i in 0..(nodes.size-1)
        nodes[i].left_parent = i-1 >= 0 ? parent_line[i-1] : null
        nodes[i].right_parent = i < parent_line.size ? parent_line[i] : null
      end
    end
    parent_line = nodes
    rows << nodes
  end
end

def max(a,b)
  if a>b then a else b end
end

for i in 1..(rows.size-1)
  rows[i].each do |node|
    left_p = (node.left_parent) ? node.left_parent.value : 0
    right_p = (node.right_parent) ? node.right_parent.value : 0
    node.value += max(node.left_parent.value, node.right_parent.value)
  end
end

final_max = rows.last.inject(0) {|m,o| if m > o.value then m else o.value end }
puts "[#{final_max} #{Time.now - st}s]"
