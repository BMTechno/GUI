count = 0
def click(count):
	
	count += 1
	print "count is :",count
	
from Tkinter import *
root = Tk()
label = Label(root, text = "python pgm")
button = Button(root, text = "click me", command = click(count = 0))
label.pack()
button.pack()
root.mainloop()
'''
from GUI_Button import add_event
#a = add_event()
print dir(add_event)
print add_event.__doc__
'''