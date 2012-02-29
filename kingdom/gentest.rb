#!/usr/bin/env ruby

def gentest(filename, n, k)
  f = File.new(filename, "w")
  f.write("#{n} #{n+1}\n")
  (n-1).times {|i| f.write("#{i+1} #{i+2}\n")}
  f.write("#{n} 1\n")
  f.write("#{k} #{n}\n") 
end

def main
  if ARGV.length < 3
    puts "Usage gentest.rb <filename> N K"
    return
  end
  gentest(ARGV[0], ARGV[1].to_i, ARGV[2].to_i)
end

main()
