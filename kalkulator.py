

# from tkinter import *
# oyna = Tk()
# oyna.title("kalkulator")
# oyna.geometry('300x300')

# natija = Label(text='natija', background='white')
# natija.place(x=50, y=50, width=100, height=30 )

# son = Entry()
# son.place(x=50 , y=90, width=100, height=30)

# def kalkulator():
#     natija.config(print(input(eval(' ')))) 

print("Pythonda kalkulator dastur:")
while True:

     a = int(input("1- son kiriting: "))
     b = int(input("2- son kiriting: "))
     
     menu = print(""" Shartlardan birini tanlang
    1. qo'shish
    2. ayirish
    3. ko'paytirish
    4. bo'lish
        """)
     
     mijoz = int(input("tanlang>>> "))
     if mijoz == 1:
         
                print(f"natija: {a}+{b}={a+b} ga teng.")
     elif mijoz == 2:
                print(f"natija: {a}-{b}={a-b} ga teng.")
     elif mijoz == 3:
                print(f"natija: {a}*{b}={a*b} ga teng.")
     elif mijoz == 4:
                print(f"natija: {a}/{b}={a/b} ga teng.")
     elif mijoz > 4:
                    print("siz faqat 4 ta shartdan birini tanlashingiz kerak!")


# tugma = Button(text='hisoblash', command=kalkulator)
# tugma.place(x=50, y=120, width=100, height=30)
# oyna.mainloop()