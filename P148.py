from tkinter import *
import random

root = Tk()
root.title('List')
root.geometry('400x400')

ListItems = Label(root)
RandomNum = Label(root)
picnicItems = ['Picnic Blanket','Picnic Basket','Cooler','Chairs']

ListItems['text'] = 'Listed Items: ' + str(picnicItems)

def stuff():
    randomNumbers = random.sample(range(0,3),1)
    RandomNum['text'] = 'Put Item Number' + str(randomNumbers) + "In Bag"
    
btn = Button(root,text = 'Which item to put in bag?', command = stuff, bg = 'orange', fg = 'black') 
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)   
ListItems.place(relx = 0.5, rely = 0.6, anchor = CENTER)  
RandomNum.place(relx = 0.5, rely = 0.7, anchor = CENTER) 

root.mainloop()






