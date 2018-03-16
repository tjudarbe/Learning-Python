#Empty list for storing aliens
aliens = []

#Make 30 aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

#Show how many aliens have been created

print("Total number of aliens: " + str(len(aliens)))

#Changing alien properties for first three aliens

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
        print(alien)
