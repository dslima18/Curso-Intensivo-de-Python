requested_toppings = ['mushrooms','french fries','extra cheese']
availabe_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
for request_topping in requested_toppings:
    if request_topping in availabe_toppings:
        print("Adding "+ request_topping+".")
    else:
        print("Sorry, we don't have" + request_topping+".")
print("\nFinished making your pizza!")
#if requested_toppings:
#    for request_topping in requested_toppings:
#        if request_topping == 'green peppers':
#            print("Sorry, we are out of green peppers right now.")
#        else:
#            print("Adding " + request_topping + ".")
#    print("\nFinished making your pizza!")
#else:
#    print("No toppings requested.")

#for request_topping in requested_toppings:
#    if request_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print("Adding "+request_topping+".")
#print("\nFinished making your pizza!")
#if 'mushrooms' in requested_topping:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_topping:
#    print("Adding pepperoni.")
#if 'extra cheese' in requested_topping:
#    print("Adding extra cheese")
#print("\nFinished making your pizza!")
#print('mushrooms' in requested_topping)
#print('pepperoni' in requested_topping)
#requested_topping = 'mushrooms'
#if requested_topping != 'anchovies':
#    print("Hold the anchovies!")