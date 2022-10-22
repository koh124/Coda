class MyClass():
  num1 = 0
  num2 = 0

  def __init__(self):
    self.num1 = 100
    self.num2 = 100
    self.add(self.num1, self.num2)
  
  def add(self, num1, num2):
    print(num1 + num2)

Myclass().add()