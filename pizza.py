'''pizza={
	'crust':'thick',
	'toppings':['mushroom', 'extra cheese'],
	}

print(f"you ordered a {pizza['crust']}-crust pizza"
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t"+topping)'''

'''def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')'''

def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")
























