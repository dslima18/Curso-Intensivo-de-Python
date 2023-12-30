#alien_0 = {'color':'green','points':5}
#alien_1 = {'color':'yellow','points':10}
#alien_2 = {'color':'red','points':15}
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow',}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color']='red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
    print("...")
print("Total number of aliens: "+str(len(aliens)))
#for alien in aliens:
#    print(alien)
#print(alien_0)
#del alien_0['points']
#print(alien_0)
#print("Original x-position: "+str(alien_0['x_position']))
#Move o alienígena para direita
#Determina a distância que o alienígena deve se deslocar de acodo com sua velocidade atual
#if alien_0['speed'] == 'slow': x_increment =1
#elif alien_0['speed'] == 'medium': x_increment=2
#else: x_increment = 3
#este deve ser um alienígena rápido
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("New x-position: " + str(alien_0['x_position']))
#print("The alien is "+ alien_0['color']+".")
#alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color']+ ".")
#alien_0['color'] = 'green'
#alien_0['points'] = 5
#print(alien_0)
#alien_0 = {'color':'green','points':5}
#print(alien_0)
#alien_0['x_position']=0
#alien_0['y_position']=25
#print(alien_0)
#print(alien_0['color'])
#print(alien_0['points'])
#new_points = alien_0['points']
#print("You just earned "+ str(new_points)+" points!")