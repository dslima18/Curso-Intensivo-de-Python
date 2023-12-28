my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
my_foods.append('cannoli')
friends_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
print("Os três primeiros elementos dessa lista são: "+str(my_foods[1:3]))
print("Os três 3 elementos do meio dessa lista são: "+str(my_foods[2:4]))
print("Os três últimos elementos dessa lista são"+str(my_foods[-3:]))
for food in my_foods:
    print(food)
print("\n")
for food in friends_foods:
    print(food)