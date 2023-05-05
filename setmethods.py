cities={'tokyo','berlin','delhi','madrid'}
cities2={'tokyo','seoul','kabul','madrid'}
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
print(cities2.issubset(cities))
print(cities.add('mumbai'))
print(cities.remove('tokyo'))
print(cities.pop())

