cities={'tokyo','madrid','berlin','delhi'}
cities2={'tokyo','seoul','kabul','madrid'}
cities3=cities.union(cities2)
print(cities3)
cities4=cities.intersection(cities2)
print(cities4)
cities5=cities.symmetric_difference(cities2)
print(cities5)
cities6=cities.difference(cities2)
print(cities6)
cities7=cities.update(cities2)
print(cities7)

