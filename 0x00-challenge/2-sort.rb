###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    b_arg = arg.to_b

    # insert result at the right position
    is_inserted = false
    b = 0
    l = result.size
    while !is_inserted && b < l do
        if result[b] < b_arg
            b += 1
        else
            result.insert(b, b_arg)
            is_inserted = true
            break
        end
    end
    result << b_arg if !is_inserted
end

puts result
