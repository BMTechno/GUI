
from Tkinter import * # Import all definitions from tkinter

class WidgetsDemo:
 def __init__(self):
 	window = Tk() # Create a window
 	window.title("Widgets Demo") # Set a title

 # Add a check button, and a radio button to frame1
 	frame1 = Frame(window) # Create and add a frame to window
 	frame1.pack()
 	self.v1 = IntVar()  # Intvar = 1 when check.....0 = unchecked
	cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1 , command = self.processCheckbutton)
	self.v2 = IntVar()  # v2 = 1 red button selected ...v2 = 2 yellow selected
	rbRed = Radiobutton(frame1, text = "Red", bg  = "red", variable = self.v2 , value = 1, command = self.processRadiobutton)
 	rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = self.v2, value = 2, command = self.processRadiobutton)
 	cbtBold.grid(row = 1, column = 1)
 	rbRed.grid(row = 1, column = 2)
 	rbYellow.grid(row = 1, column = 3)

 # Add a label, an entry, a button, and a message to frame1
 	frame2 = Frame(window) # Create and add a frame to window
 	frame2.pack()
 	label = Label(frame2, text = "Enter your name: ") #create label
 	self.name = StringVar()   #enter string val
 	entryName = Entry(frame2, textvariable = self.name )  # enter string and store in 'entryname' variable
 	btGetName = Button(frame2, text = "Get Name", command = self.processButton) #create button to take data
 	message = Message(frame2, text = "It is a widgets demo") # it takes words and display
 	label.grid(row = 1, column = 1)   # grid is to set location of widget on window
 	entryName.grid(row = 1, column = 2)
 	btGetName.grid(row = 1, column = 3)
 	message.grid(row = 1, column = 4)

 # Add text
 	text = Text(window) # create text widget to display and editing text 
 	text.pack()
 	text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
 	text.insert(END, "these carefully designed examples and use them ")
 	text.insert(END, "to create your applications.")

 	window.mainloop() # Create an event loop
 	  #or
 	#mainloop()

 def processCheckbutton(self):
 	print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

 def processRadiobutton(self):
 	print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected " )

 def processButton(self):
 	print("Your name is " + self.name.get())

WidgetsDemo() # Create GUI
