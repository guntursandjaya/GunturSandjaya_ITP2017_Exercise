place = ['Hong Kong','Bali','Japan','London','Raja Ampat']
print(sorted(place))

place.reverse()
print(place)

place.append('Bandung')
print(place)

del place[1]
print(place)

popped_place = place.pop()

print(popped_place)

place.remove('Raja Ampat')
print(place)

print(len(place))
