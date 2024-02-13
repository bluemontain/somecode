requested_toppings = ['mushrooms','green pepers','olives',
                      'pepperoni','pineapple','extra cheese']
"""
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese.")

print("Finished making your pizza!\n")

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
elif "extra cheese" in requested_toppings:
	print("Adding extra cheese.")

print("Finished making your pizza!")
"""
#requested_toppings = []
if requested_toppings:

    for requested_topping in requested_toppings:
    	if requested_topping == 'green pepers':
    			print("Sorry, we are out of green peppers right now.")
    	else:
             print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza？")