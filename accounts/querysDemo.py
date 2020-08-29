from accounts.models import *

# to access all customers
customers = Customer.objects.all()

customer1 = Customer.objects.get(name="Kiran Paithane")