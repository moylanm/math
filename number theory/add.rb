# frozen_string_literal: true

require 'optparse'

def add(num_a, num_b)
  temp_a = num_a.split('').map(&:to_i)
  temp_b = num_b.split('').map(&:to_i)

  c = 0
  s = []

  temp_a.reverse.zip(temp_b.reverse).each do |pair|
    d = ((pair[0] + pair[1] + c) / 2).floor
    s.push(pair[0] + pair[1] + c - 2 * d)
    c = d
  end
  s.push(c)

  s.reverse.join('')
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: add.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-b', '--bit-strings STRINGS', Array, 'Binary strings.') do |bit_strings|
      options[:bit_strings] = bit_strings
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:bit_strings].nil?

  puts add(options[:bit_strings][0], options[:bit_strings][1])
end
