sanwich_orders = ['beef_sandwich','meet_sandwich','fish_sandwich','potato_sanwich','pastrami','pastrami','pastrami']
finished_sanwiches = []

print("THe pastrami has sold out.")
pastrami_on = True
pat = 'pastrami'
while pastrami_on:
	if pat in sanwich_orders:
		sanwich_orders.pop()
	else:
		pastrami_on = False

for sanwich in sanwich_orders:
	finished_sanwiches.append(sanwich)
	print(f"\nI mad your {sanwich} sanwich")