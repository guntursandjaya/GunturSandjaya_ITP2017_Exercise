my_pizzas = ['Pepperoni','Cheese','Meat','Vegetable']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Chicken')
friend_pizzas.append('Salmon')

print('My Favorite Pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print('\n')

print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
