from Tkinter import *
class add_event :
	'''click button for click event and cancel event'''
	def __init__(self):
		window = Tk()
		window.title("Title")
		label = Label(window, text = "Button" , fg = "white", bg = "black")
		button_click = Button(window, text = "click", fg = "orange", command = self.click)
		button_cancel = Button(window, text = "cancel", bg = "red", command = self.cancel)
		label.pack()
		button_click.pack()
		button_cancel.pack()
		window.mainloop()
	def click(self):
		print "button clicked"
	def cancel(self):
		print "process canceled"	

print '''
      There are two advantages of defining a class for creating a GUI and processing GUI
events. First, you can reuse the class in the future. Second, defining all the functions as methods
enables them to access instance data fields in the class.'''
#a = add_event() 