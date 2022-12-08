# frozen_string_literal: true

require 'optparse'

$CHAR_MAP = {
  'A' => 10,
  'B' => 11,
  'C' => 12,
  'D' => 13,
  'E' => 14,
  'F' => 15
}.freeze

def hex_to_bin(num)
  arr = num.split('').map do |c|
    $CHAR_MAP.key?(c) ? $CHAR_MAP[c] : c.to_i
  end

  arr.map do |n|
    n.to_s(2).rjust(4, '0')
  end.join('')
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: hex_to_bin.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-n', '--number NUMBER', String) do |number|
      options[:number] = number
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:number].nil?

  puts "$(#{options[:number].upcase})_{16} = (#{hex_to_bin(options[:number].upcase)})_2$"
end
