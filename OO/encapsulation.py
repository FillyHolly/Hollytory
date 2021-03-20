class Phone_1:
	number = "111-11-11"
	def print_number(self):
		print("Phone number is: ", self.number)

class Phone_2:
	username = "Kate" # public variable
	__how_many_times_turned_on = 0 # private variable

	def call(self): # public method
		print("Ring-ring!")

	def __turn_on(self): # private method
		self.__how_many_times_turned_on += 1
		print("Time was turned on: ", self.__how_many_times_turned_on)

# my_phone = Phone_1()
# my_phone.print_number()

my_phone = Phone_2()

my_phone.call()
print("The username is ", my_phone.username)
# print("Turned on: ", my_phone.__how_many_times_turned_on)
print("Turned on: ", my_phone._Phone_2__how_many_times_turned_on)
