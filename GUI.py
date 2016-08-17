from Tkinter import *
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.check_var = BooleanVar()
		check = Checkbutton(frame, text='Pin 18',
		command=self.update,
		variable=self.check_var, onvalue=True, offvalue=False)
		check.grid(row=3)

		Label(frame, text='Red').grid(row=0, column=0)
		Label(frame, text='Green').grid(row=1, column=0)
		Label(frame, text='Blue').grid(row=2, column=0)
		scaleRed = Scale(frame, from_=0, to=100,orient=HORIZONTAL, command=self.updater)
		scaleRed.grid(row=0, column=1)
		print scaleRed
		scaleGreen = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.updateg)
		scaleGreen.grid(row=1, column=1)
		scaleBlue = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.updateg)
		scaleBlue.grid(row=2, column=1)	
		
	def update(self):
		print "got it"
	def updater(self, scaleRed):
		print "got it r"
	def updateg(self, master):
		print "got it g"		
	
root = Tk()
root.wm_title('On / Off Switch')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()