# frozen_string_literal: true

require 'optparse'

def dec_to_bin(num, verbose)
  quotient = num
  arr = []

  until quotient.zero?
    puts "$#{quotient} / 2 = #{quotient / 2}$, $#{quotient} \\bmod 2 = #{quotient % 2}$ \\\\" if verbose

    arr.push(quotient % 2)
    quotient /= 2
  end

  arr.reverse
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: dec_to_bin.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-n', '--number NUMBER', Integer) do |number|
      options[:number] = number
    end
    parser.on('-v', '--verbose', TrueClass, 'Rub verbosely') do |v|
      options[:verbose] = v.nil? ? true : v
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:number].nil?

  puts "\n$#{options[:number]} = (#{dec_to_bin(options[:number], options[:verbose]).join('')})_2$"
end
