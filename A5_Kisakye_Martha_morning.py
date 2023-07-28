#KISAKYE MARTHA JANEPHER
#21/U/10006/EVE
#2100710006

#Exercise use inheritance to calculate the area and perimeter of a circle

#Method overriding
"""class Animal:
    def make_sound(self):
        print("Animal is making sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
        
class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")
        
def make_animal_sound(animal):
    animal.make_sound()
#Create a objects
animal = Animal()
dog = Dog()
cat = Cat()

#Calling make_animal_sound
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

#polymophism
class Shape:
    def calculate_area(self):
        pass
class Rectangle:
    def __init__(self, length , width) :
       self.length = length
       self.width = width
    def calculate_area(self):
        return self.width*self.length
    
class Circle(Shape):
    def __init__(self, radius) :
        self.radius = radius
    def calculate_area(self):
        return 3.14*self.radius**2
    def calculate_circumference(self):
        return 2* 3.14 * self.radius
    
#create shapes
rectangle = Rectangle(5,5)    
circle = Circle(5)

#Display area
print("Area of Rectangle is:", rectangle.calculate_area())
print("Area of Circle is:", circle.calculate_area())

#Exercise2 Demonstrate bstraction using calculating area of a circle and rectangle
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle:
    def __init__(self, length , width) :
       self.length = length
       self.width = width
    def calculate_area(self):
        return self.width*self.length
    
class Circle(Shape):
    def __init__(self, radius) :
        self.radius = radius
    def calculate_area(self):
        return 3.14*self.radius**2
    def calculate_circumference(self):
        return 2* 3.14 * self.radius
    
rectangle = Rectangle(15,5)    
circle = Circle(8)

#Display area
print("Area of Rectangle is:", rectangle.calculate_area())
print("Area of Circle is:", circle.calculate_area())

 """    

#receipt printing programing with GUI interface
from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("receipt slip")
root.geometry('1280x720')
bg_color='#000000'

#variable
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Cost=IntVar()
quantity=IntVar()
receipt_no=StringVar()
x=random.randint(1000,9999)
receipt_no.set(str(x))

global l
l=[]

#Functions

def additm():
    n=Cost.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please enter item')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n======================================")
        save_bill()



def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Cost.set(0)
    quantity.set(0)
    welcome()
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
def save_bill():
    op=messagebox.askyesno("Save receipt","Do you want t o save the Receipt?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(receipt_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"receipt no, :{receipt_no.get()} Saved Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t  Welcome to MarthaK supermarket")
    textarea.insert(END,f"\n\nreceipt Number:\t\t{receipt_no.get()}")
    textarea.insert(END,f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n======================================")
    textarea.insert(END,"\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n======================================\n")
    textarea.configure(font='arial 15 bold')
   



title=Label(root,pady=2,text="Martha K supermarket",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#Product Frames
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='white',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='white',bg=bg_color)
F2.place(x=20, y=180,width=630,height=500)

itm= Label(F2, text='Product Name', font=('times new romon',18, 'bold'), bg=bg_color, fg='white').grid(
row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20,textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1, padx=10,pady=20)

cost= Label(F2, text='Product Cost', font=('times new romon',18, 'bold'), bg=bg_color, fg='white').grid(
row=1, column=0, padx=30, pady=20)
cost_txt = Entry(F2, width=20,textvariable=Cost, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,pady=20)

n= Label(F2, text='Product Quantity', font=('times new romon',18, 'bold'), bg=bg_color, fg='white').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)

#========================Bill area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

receipt_title=Label(F3,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Add item',font='arial 15 bold',command=additm,padx=5,pady=10,bg='white',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate Receipt',font='arial 15 bold',command=gbill,padx=5,pady=10,bg='white',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='white',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='white',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)


root.mainloop()
