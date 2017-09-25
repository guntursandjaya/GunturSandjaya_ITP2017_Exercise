guest = ['Ariel','Jason','Akbar','Denny']
mail = ", You are invited to dinner"
guest.insert(0,'Faris')
guest.insert(2,'Handi')
guest.append('Yoksan')
print(guest[0] + mail)
print(guest[1] + mail)
print(guest[2] + mail)
print(guest[3] + mail)
print(guest[4] + mail)
print(guest[6] + mail)


massage = 'i found bigger table for us'
print(massage)

text = 'I am sorry that i cannot invite you to dinner because there is no more table'
print(text)
guest.pop()
guest.pop()
guest.pop()
guest.pop()
print(guest)

massage = ',You are still invited to dinner'
print(guest[0] + massage)
print(guest[1] + massage)
print(guest[2] + massage)

del guest[0]
del guest[0]
del guest[0]
print(guest)

