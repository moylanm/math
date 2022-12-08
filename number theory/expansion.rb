# frozen_string_literal: true

require 'optparse'

# A simple proof of concept for constructing base b expansions of integers
class Expansion
  CHAR_MAP = {
    10 => 'A',
    11 => 'B',
    12 => 'C',
    13 => 'D',
    14 => 'E',
    15 => 'F'
  }.freeze

  def initialize(number, base)
    raise ArgumentError if base < 2

    @number = number
    @base = base
  end

  def self.expansion(number, base)
    new(number, base).expansion
  end

  def expansion
    quotient = @number
    arr = []

    until quotient.zero?
      arr.push(quotient % @base)
      quotient /= @base
    end

    map_chars(arr) if @base == 16

    arr.reverse.join('')
  end

  private

  def map_chars(array)
    array.map! do |num|
      num > 9 ? CHAR_MAP[num] : num
    end
  end
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: expansion.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-n', '--number NUMBER', Integer) do |number|
      options[:number] = number
    end
    parser.on('-b', '--base BASE', Integer) do |base|
      options[:base] = base
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:number].nil?
  raise OptionParser::MissingArgument if options[:base].nil?

  p "#{options[:number]} = (#{Expansion.expansion(options[:number], options[:base])})_#{options[:base]}"
end
