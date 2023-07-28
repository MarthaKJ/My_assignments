#KISAKYE MARTHA JANEPHER
#2100710006
#21/U/10006/EVE

print("Welcome")
student_name=input("Please enter your name")

print(f"Hello , {student_name}, on a scale of 1 to 10, how are you currently feeling")

scale = int(input("Please rate your mental health"))
64
if scale < 1 or scale >10 :
    print("Invalid please enter anumber between 1 and 10")
else :
    print(f"Thank you for sharing, {student_name}")
    
    if scale <= 3 :
        print("We are sorry to hera that you aint feeling very okay")
        print("Please try to contact health proffesionls for assistance")
        
    elif scale >=4 or scale <= 6 :
        print(f"thats fair {student_name}")
        print("Please add in some little effort")
        
        
    else:
        print(f"Woow glad to hear tht {student_name}")
        print("Keep up with the good work")
        
        