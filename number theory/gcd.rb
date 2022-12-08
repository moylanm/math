# frozen_string_literal: true

require 'optparse'

def gcd(a, b)
  x = a
  y = b

  until y.zero?
    puts "#{x} = #{x / y} * #{y} + #{x % y}"
    r = x % y
    x = y
    y = r
  end

  x
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: gcd.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-n', '--numbers NUMBERS', Array) do |numbers|
      options[:numbers] = numbers
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:numbers].nil?

  puts gcd(options[:numbers][0].to_i, options[:numbers][1].to_i)
end
