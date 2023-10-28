class encapsulation(object):
      #We need to create the object value and call with the instance self
      #Set_val acts as gateway to tranfer value
      def set_val(self, val):
          self.value = val

      #get val is the gateway that recieves the value
      def get_val(self):
          return self.value

#Creating instance from the class encapsulation
a=encapsulation()
b=encapsulation()

#Setting the value by calling the class
a.set_val(10)
b.set_val(100)

#Assiging hello string to the value object
a.value = 'Hello'

#print the values
print(a.get_val())
print(b.get_val())
