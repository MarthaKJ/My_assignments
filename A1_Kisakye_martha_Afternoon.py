#KISAKYE MARTHA JANEPHER
#21/U/10006/EVE
#2100710006


girls = {"Martha", "Daphne","Cathy", "Gloria"}
print(girls)

#length
print(len(girls))

#datatype of the set
print(type(girls))

if "Martha" in girls:
    print("Martha is present")
    
#Adding items in a set
#Here we use the add() method

girls.add("Ruth")
print(girls)

#adding two sets together
#use the union operator "|"

boys = {"Sheldon", "Thor", "Rahul"}
print(girls|boys)

#or use the update()method
girls.update(boys)
print(girls)


#tuples
phones = ("samsung", "iphone", "techno")
print(phones)

print(len(phones))

#accessing tuple
#accessing tuples with a single element by index
phone2 = phones[1]
print(phone2)

#accessing multiple using slicing

multiple = phones[0:2]
print(multiple)

#accessing the last element

last = phones[-1]
print(last)

