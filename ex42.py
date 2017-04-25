## Animal is-a object (yes, short of consusing) look at the extra credi

class Animal(object):
	pass

## ??m
class Dog(Animal):

	## ??
	def __init__(self, name):
		self.name = name
## ??
class Cat(Animal):

	## ??
	def __init__(self, name):
		self.name = name
		
## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name
	
		## person has a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary
	
## Fish is-an  object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish	
class Halibut(Fish):
	pass

	
## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat 
satan = Cat("Satan")

## mary is-a  Person
mary = Person("Mary")

## Mary has a pet, Satan (object = satan)
mary.pet = satan

## Frank is an employee.  He has-a salary of 120k
frank = Employee("Frank", 120000)

## Frank has-a pet, rover.
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()


