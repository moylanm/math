# frozen_string_literal: true

require 'optparse'

def oct_to_bin(num)
  num.digits.map do |n|
    n.to_s(2).rjust(3, '0')
  end.reverse.join('')
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: oct_to_bin.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-n', '--number NUMBER', Integer) do |number|
      options[:number] = number
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:number].nil?

  puts "\n$(#{options[:number]})_8 = (#{oct_to_bin(options[:number])})_2$"
end
