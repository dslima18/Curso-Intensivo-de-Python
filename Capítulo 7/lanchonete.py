sandwich_orders = ['pastrami','pastrami','pastrami','big mac']
print("Estamos sem pastrami.")
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
    print("O seguinte sanduíche está pronto: "+finished_sandwich)
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
print("Os sanduíches que estão pronto são: "+str(finished_sandwiches))