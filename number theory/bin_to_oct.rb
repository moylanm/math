# frozen_string_literal: true

require 'optparse'

def bin_to_oct(bit_str)
  dec = 0
  arr = []

  bit_str.split('').reverse.each_with_index do |bit, idx|
    dec += 2**idx if bit == '1'
  end

  until dec.zero?
    arr.push(dec % 8)
    dec /= 8
  end

  arr.reverse.join('')
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: bin_to_oct.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-b', '--bit-string STRING', String) do |bit_string|
      options[:bit_string] = bit_string
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:bit_string].nil?

  puts "\n$(#{options[:bit_string]})_2 = (#{bin_to_oct(options[:bit_string])})_8$"
end
