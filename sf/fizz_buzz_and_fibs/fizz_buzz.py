# Iterates the integers from 1 to 50. For multiples of three print "Fizz"
# instead of the number and for multiples of five print "Buzz" instead of
# the number. For numbers that are multiples of three and five, print "FizzBuzz".

for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)