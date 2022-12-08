# frozen_string_literal: true

require 'optparse'

$CHAR_MAP = {
  10 => 'A',
  11 => 'B',
  12 => 'C',
  13 => 'D',
  14 => 'E',
  15 => 'F'
}.freeze

def bin_to_hex(bit_str)
  dec = 0
  arr = []

  bit_str.chars.reverse.each_with_index do |bit, idx|
    dec += 2**idx if bit == '1'
  end

  until dec.zero?
    arr.push(dec % 16)
    dec /= 16
  end

  arr.map! do |num|
    num > 9 ? $CHAR_MAP[num] : num
  end

  arr.reverse.join('')
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: bin_to_hex.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-b', '--bit-string STRING', String) do |bit_string|
      options[:bit_string] = bit_string
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:bit_string].nil?

  puts "$(#{options[:bit_string]})_2 = (#{bin_to_hex(options[:bit_string])})_{16}$"
end
