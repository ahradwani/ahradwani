"""
To run Python code you need to copy | paste the code in your  python local editor, 
or just use one of the python online interpreter. Here are some links for 
python online compyler.


https://www.online-python.com/

https://www.programiz.com/python-programming/online-compiler/

https://www.onlinegdb.com/online_python_compilAb


copy and run the code, change to see the efficts.

About:
   Python lesson about Class for fruit
   we will collect the fruit Name, hwo maney we have of it, and its price.            


Created in: 10.6.2026
Powered By:  AHRADWANI.fun | Learning Hub.


"""

class Fruit:
  def __init__ (self,name,count,cost):
    self.name = name
    self.cost = cost
    self.count = count

  def sale(self,sale_price):
      cp = self.cost  # the current price
      
      self.cost = self.cost * sale_price 
      if self.cost < cp :
          return f"The New SALE price of the {self.name} is {self.cost}." 
      else:
           return f"The New Price of the {self.name} is {self.cost}." 

  def sell (self,amount):
        self.count = self.count - amount
        return f"We sell {amount} of {self}, now we have {self.count} in stock." 
      
  def __str__(self):
    return f'{self.name} we have {self.count} peaces ,the price is {self.cost}'

# calling the class for Apple, and Banana
apple = Fruit('Apple',10,2.5)
banana = Fruit('Banana',20,3.6)

# calling the sale function for the Apple
print(Fruit.sale(apple,0.5))  # reduce the price of the apples by 0.5

#calling the sell function for the Apple
Fruit.sell(apple,6)

# call the sale function to adjust the price of the Apple
Fruit.sale(apple,1.5)



