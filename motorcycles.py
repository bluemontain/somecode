motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'HaoJue')
print(motorcycles)

#del motorcycles[0]
#popped_motorcycles = motorcycles.pop()
#last_owned = motorcycles.pop()
#print(motorcycles)

#print(f"The last motorcycles I owned was a {last_owned.title()}.")
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

