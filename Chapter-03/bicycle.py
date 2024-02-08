bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
#In a list the starting position (index) is 0. 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[3].upper())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
#By using a [-1] Python will give you the last input on the list
#The same applys for [-2] giving you the second to last (more convinent then finding where they are on the list)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " +bicycles[3].title() + "."

print(message)