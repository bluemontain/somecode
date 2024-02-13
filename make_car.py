def make_car(manufacturer,model,**cars_info):
	cars_info['manufacturer'] = manufacturer
	cars_info['model'] = model
	return cars_info

car = make_car('subaru','outback',
	          color='blue',
              tow_package=True
	          )

print(car)
