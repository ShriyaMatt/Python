class myClass:
  # private variable
  __privateVar=27;
  # private method
  def _privMeth(self):
    print("I am inside class myClass")
  # function to print private of private variable
  def hello(self):
    print("Private Varaible Value:",myClass.__privateVar)

#object creation and method call
foo=myClass()
foo.hello()
foo.__privMeth