for i in range(100):
  if i % 15 == 0:
    print('FizzBuzz\n')
  elif i % 3 == 0:
    print('Fizz\n')
  elif i % 5 == 0:
    print('Buzz\n')
  else:
    print(i, end="\n")
