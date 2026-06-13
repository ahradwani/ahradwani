""
Python Class


""

class fruit:
  def __init__ (self,name,count,cost):
    self.name = name
    self.cost = cost
    self.count = count

  def sale(self,sale_price):
    return self * sale_price

  def sell (self,amount):
    return self.count - amount
  
