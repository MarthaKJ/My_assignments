#KISAKYE MARTHA JANEPHER
#2100710006
#21/U/10006/EVE

#dictionaries
#Exercise 1 . use values() method to return a list of all values in a dictionary

grades = {
    'Martha':90,
    'Brian': 95,
    'Dana': 99,
    'Tum': 67
}

grade_list = list(grades.values())
print(grade_list)

#Exercise 2 To check if a key word exists in the dictionary

key = 'Martha'
if key in grades:
    print(f"{key}exists in the dictionary")
    
else:
    print(f"{key} doesnt exist in the dictionary")
    
#Exercise 3 how to change dictionary items, how to update
key_change = 'Dana'
new_grades = 89

if key_change in grades:
    grades[key_change] = new_grades
    print(f"The grade for {key_change} is now {new_grades}")
else:
    print(f"{key_change} doesnt exit in the dictionary")
    
print(grades)

#Exercise 4 How to add and remoe items in a dictionary
#adding items

grades['Frank']= 75
grades['Heli'] = 80

print(grades)

#removing
del grades['Martha']
print(grades)

#Exercise 5 How you can loop through a dictionary and how to nest dictionary strings

for key, value in grades.items():
    print(f"{key} : {value}")
    
#nesting
attendee = {
    'name': 'Dana',
    'age' : 20,
    'address': {
        'street': '1234 Main st' ,
        'city' :'Jinja',
        'country': 'Uganda'
        
    }
}
print(attendee)


#STRINGS EXERCISE
#Exercise1 use the len()function to determine the length of a string

mine = "I am the best"
print(len(mine))

#Exercise 2 give an example of using a for loop in string

for me in mine:
    print(me)
    
#Exercise 3 give an example of slicing in strings
slice = mine[5:12]
print(slice)

#Exercis Use a condition to show how to use booleans 
m = 6
k = 10

if m < k:
    print(True)
else:
    print(False)