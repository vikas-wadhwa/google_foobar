numbers = [1,2,3,4,5,6,7,8,9]
n = Array(2..10)
i = [0,1,2,3,4,5,6,7,8,9]

n.each do |n|

  new_numbers = []

  numbers.each do |x|

    digits = i - x.to_s.split('').map(&:to_i)

    digits.each do |d|

      test = x.to_s + d.to_s


      if test.to_i % n == 0
        new_numbers.push(test)
        puts test + ' is divisible by ' + n.to_s
      end

    end


  end




  unless numbers == new_numbers
    numbers = new_numbers.clone
  end

end