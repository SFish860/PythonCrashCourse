motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
#line 4 changes the value of 'honda' to 'ducati'

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
#line 11 adds 'ducati' to the end of the list without affecting any other element in the list

motorcycles = []
#You can add to empty lists
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
#lines 17-20 are adding to the empty list
print(motorcycles)
#This is usefull when you don't know the data that will be used until after the program is created

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
#By using insert(0-the position of insert, 'name of insert') will isert ti the list at the position specified and move othere values one to the right

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #pop a value from the list and store that value in the variable popped_motorcycle.
print(motorcycles) #shows that a value has been removed from the list
print(popped_motorcycle) #shows that we still have access to the value that was removed

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop() #adding postion to change output
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') #By using the name of the variable python will find the position and remove it 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) #'ducati' is removed from the list but still stored in too_expensive
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
#If the value is listed more than once you will have to use a loop to remove