
import sys
print(sys.executable)
print(sys.version)


class Employee:
	"""A sample Employee class"""

	def _init_(self, first, last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return '{} {}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('john', 'smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
	
