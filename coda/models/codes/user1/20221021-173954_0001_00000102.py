for i in range(0, 10):
  print(i * 2)

class myClass():
  num1 = 0
  num2 = 0
  
  def __init__(self, arg1, arg2):
    self.num1 = arg1
    self.num2 = arg2

  def call():
    self.addition(self.num1, self.num2)

  def addition(self, arg1, arg2):
    print(arg1 + arg2)

myClass(100, 150).call()


