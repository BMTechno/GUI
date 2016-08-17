from Tkinter import *

class App:
	
	def __init__(self):
		self.count = 0
		window = Tk()
		window.title("Scale")
		frame = Frame(window)
		frame.pack()
		
		#Label(frame, text = "Scale1").grid(row = 0, column = 0)
		scale = Scale(frame, from_= 0, to = 180, orient = HORIZONTAL, command = self.update)
		scale2 = Scale(frame, from_= 0, to = 180, orient = HORIZONTAL, command = self.update)
		message = Message(frame, text = "It's scale")
		scale.grid(row = 0, column = 1)
		scale2.grid(row = 1, column = 1)
		#message.grid(row = 1, column = 1)
		scale.pack()
		scale2.pack()
		window.mainloop()

	def update(self, scale):
		self.count = self.count + 1
		#print self.count
		print scale
		#pulse_len = int(float(scale) * 500.0 / 180.0) + 110
       # print angle
App()		
