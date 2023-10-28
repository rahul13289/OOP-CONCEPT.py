class animal(object):

    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print('%s is eating %s' % (self.name,food))

class dog(animal):
    def fetch(self,thing):
        print('%s shreds the string!' % (self.thing))
class cat(animal):
    def swatstring(self):
        print('%s shreds the string!' % (self.name))

r=dog('rover')
f=cat('fluffy')

#Rover goes after the paper
r.fetch('paper')

#Fluffy shreds the string
f.swatstring()
r.eat('dog food')
f.eat('cat food')
r.swatstring()
















#class Date(object):
 #   def get_date(self):
  #      return '2014-10-13'

#Inherits from the date class
#class Time(Date):
   # def get_time(self):
    #    return '08:13:07'


#dt=Date()
#print(dt.get_date())


#tm=Time()

#found this method in the date class
#print(tm.get_time())
#print(tm.get_date())