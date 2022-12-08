# frozen_string_literal: true

require 'optparse'

def mod_exp(b, n, m)
  a = n.to_s(2).split('').map(&:to_i)
  x = 1
  power = b % m

  a.reverse.each do |i|
    x = (x * power) % m if i == 1
    power = (power * power) % m
  end

  x
end

if $PROGRAM_NAME == __FILE__

  options = {}
  OptionParser.new do |parser|
    parser.banner = 'Usage: mod_exp.rb [options]'

    parser.on_tail('-h', '--help', 'Show this message.') do
      puts parser
      exit
    end

    parser.on('-b', '--base NUMBER', Integer) do |base|
      options[:base] = base
    end
    parser.on('-e', '--exponent EXPONENT', Integer) do |exponent|
      options[:exponent] = exponent
    end
    parser.on('-m', '--mod MOD', Integer) do |mod|
      options[:mod] = mod
    end
  end.parse!

  raise OptionParser::MissingArgument if options[:base].nil?
  raise OptionParser::MissingArgument if options[:exponent].nil?
  raise OptionParser::MissingArgument if options[:mod].nil?

  puts mod_exp(options[:base], options[:exponent], options[:mod])
end
