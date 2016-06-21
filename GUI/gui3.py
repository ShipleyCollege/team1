
from tkinter import *
from tkinter.ttk import *

root = Tk()

class App():
	def __init__(self):
		root.geometry("500x430")
		root.configure(bg='#ececec')
		
		root.minsize(400, 350)	
		
		self.frame1 = Frame(root)
		self.frame2 = Frame(root)
		self.frame1.tkraise()

		self.inputTab();
		
		
		self.run_widget()
		

	def inputTab(self):
		self.input_widget()
		self.output_widget()
		self.blank_widget()
		

	def input_widget(self):
		label_input = Label(self.frame1, text="Input").grid(row="0")
		list_input = ["Clipboard", "Blank", "test"]
		self.var_input = StringVar()
		self.var_input.set(list_input[0]) # default value
		drop_input = OptionMenu(self.frame1, self.var_input, *list_input).grid(row="0", column="1")

	def clipboard_widget(self):
		cliptext = self.frame1.clipboard_get()
		label_clip = Label(self.frame1, text = cliptext).grid(row="0", column="2")

	def blank11(self):
		print("11")

	def blank12(self):
		print("12")

	def blank_widget(self):
		label_input = Label(self.frame1, text="Columns").grid(row="5")

		v = IntVar()
		Radiobutton(self.frame1, text="1 Line 1 Column", variable=v, value=1, command = self.blank11).grid(row=6, column=1) 
		Radiobutton(self.frame1, text="1 Line 2 Column", variable=v, value=2, command = self.blank12).grid(row=7, column=2)
        
	def output_widget(self):
		label_output = Label(self.frame1, text="Output Type").grid(row="1")
		list_output = ["Compact","Exploded","Exploded Lego"] #read in folder which contains the output types in then when a new one is created it will be added to the list
		var_output = StringVar()
		var_output.set(list_output[0]) # default value
		drop_output = OptionMenu(self.frame1, var_output, *list_output).grid(row="1", column="1")

	def nextHit(self):
		print("value is", self.var_input.get())
		
		#master.quit()

	def run_widget(self):
		button_run = Button(self.frame1, text="Next", command=self.nextHit).grid(row="10", column="4", sticky="s,e") #runs the program based on the output method chosen, and reads in the input choice



        
#class Run():
#	app = App()

if __name__ == "__main__":
#	root = tk.Tk()
	root.title('Project ViP Wizard')
	app = App()	
	
	root.mainloop()

