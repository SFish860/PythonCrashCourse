#friends = ['john', 'jack', 'josh', 'jimmy' ]
#print(friends[0].title())
#print(friends[1].title())
#print(friends[-2].title())
#print(friends[-1].title())

#friends = ['john', 'jack', 'josh', 'jimmy' ]
#message = "Hi, my friends name is " + friends[0].title() + "."
#message_1 = "Hi, my friends name is " + friends[-3].title() + "."
#message_2 = "Hi, my friends name is " + friends[3].title() + "."
#message_3 = "Hi, my friends name is " + friends[-1].title() + "."

#print(message)
#print(message_1)
#print(message_2)
#print(message_3)

#brands = ['kawasaki', 'honda', 'yamaha','suzuki', 'husqvarna']
#message = "I would like to own a " + brands[0].title() + " motorcyle."

#print(message)

#guests = ['john', 'jack', 'josh', 'jimmy' ]
#message = "Hello " + guests[0].title() + ", you are invited to dinner at 7 p.m."

#print(message)

guests = ['john', 'jack', 'josh', 'jimmy' ]

message = "Hello everyone, " + guests[0].title() + " can't make the it to dinner."
print(message)

guests = ['john', 'jack', 'josh', 'jimmy' ]
guests[0] = 'marry'

message = guests[0].title() + " , you are invited to dinner at 7 p.m."
print(message)
message = guests[1].title() + " , you are invited to dinner at 7 p.m."
print(message)
message = guests[2].title() + " , you are invited to dinner at 7 p.m."
print(message)
message = guests[3].title() + " , you are invited to dinner at 7 p.m."
print(message)

guests = ['john', 'jack', 'josh', 'jimmy' ]
guests.insert(0, 'jerry')
guests.insert(2, 'jack')
guests.append('johny')
print(guests)

message = "Hello " + guests[0].title() + ", you are invited to dinner at 7 p.m."
print(message)
message = "Hello " + guests[2].title() + ", you are invited to dinner at 7 p.m."
print(message)
message = "Hello " + guests[-1].title() + ", you are invited to dinner at 7 p.m."
print(message)
message_1 = "Hello " + guests[1].title() + ", I have found a bigger table for dinner."
print(message_1)
message_1 = "Hello " + guests[3].title() + ", I have found a bigger table for dinner."
print(message_1)
message_1 = "Hello " + guests[4].title() + ", I have found a bigger table for dinner."
print(message_1)

guests = ['john', 'jack', 'josh', 'jimmy']
no_invite = guests.pop(0)
message = "Hello " + no_invite.title() + ", sorry I only have room for two at dinner."
print(message)
no_invite = guests.pop(-1)
message = "Hello " + no_invite.title() + ", sorry I only have room for two at dinner."
print(message)

message = "Hello " + guests[0].title() + ", you are still invited to dinner."
print(message)
message = "Hello " + guests[-1].title() + ", you are still invited to dinner."
print(message)