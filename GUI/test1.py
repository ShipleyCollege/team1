from tkinter import *
from tkinter.ttk import *
 

### got to get output option to 2 if text is entered.
### run code at runIt


def raise_frame(frame):
	frame.tkraise()
	

def clipboard():
	print("clipboard")
	
def filename(fn):
	print("filename : " + fn.get())	
	v.set(2)

def filenameOut(fn):
	print("filename out : " + fn.get())	

def blank():
	print("blank")
	v.set(3)
	blankNodeValue.set(getBlankDesc(rc))

def getBlankDesc(option):
	row = 1
	col = option.get()
	if option.get() > 5:
		row = 2
		col = option.get() - 5
	return "[Currently " + str(row) + " row, " + str(col) + " column]"

def outputType():
	print(ot.get())
	

root = Tk()
root.geometry("500x500")
root.configure(bg='#ececec')
root.minsize(450, 350)	

s = Style()
s.configure('My.TFrame', background='red')

f1 = Frame(root, style='My.TFrame')
f2 = Frame(root)
f3 = Frame(root)
# which input option is selected
v = IntVar()
v.set(1)
# which blank option is selected
rc = IntVar()
rc.set(1)
# filename input
filenameInput = StringVar()
filenameInput.trace("w", lambda name, index, mode, sv=filenameInput: filename(filenameInput))
# output type
ot = IntVar()
ot.set(1)
# filename output
filenameOutput = StringVar()
filenameOutput.trace("w", lambda name, index, mode, sv=filenameOutput: filenameOut(filenameOutput))



blankNodeValue = StringVar()
blankNodeValue.set(getBlankDesc(rc))

for frame in (f1, f2, f3):
	frame.grid(row=0, column=0, sticky='news')
#line 0
Label(f1, text="           ").grid(row="0", column="0")
Label(f1, text="           ").grid(row="0", column="1")
Label(f1, text="           ").grid(row="0", column="2")
Label(f1, text="           ").grid(row="0", column="3")
Label(f1, text="           ").grid(row="0", column="4")
Label(f1, text="           ").grid(row="0", column="5")
Label(f1, text="           ").grid(row="0", column="6")
Label(f1, text="           ").grid(row="0", column="7")
#line 1
Label(f1, text="           Project ViP - GUI").grid(row="1", column="2")
Label(f1, text="V0.7").grid(row="1", column="4")
#line 2
Label(f1, text=" ").grid(row="2", column="0", sticky="N, W")
#line 3
Label(f1, text=" Please choose an input source;").grid(row="3", column="0", sticky="W", columnspan="3")
#line 4
Label(f1, text=" ").grid(row="4", column="0")
#line 5
Radiobutton(f1, text="Clipboard", variable=v, value=1, command = clipboard).grid(row="5", column="1") 
#line 6
Label(f1, text="In the Unreal Engine 4 Blueprint Editor, select the nodes you").grid(row="6", column="1", columnspan="6", sticky="w")
#line 7
Label(f1, text="want to print and hit ctrl-C to copy them to the clipboard first. ").grid(row="7", column="1", columnspan="6", sticky="w")
#line 8
Label(f1, text=" ").grid(row="8", column="0")
#line 9
Radiobutton(f1, text="File", variable=v, value=2, command = clipboard).grid(row="9", column="1", sticky="w") 
#line 10
Label(f1, text="Filename : ").grid(row="10", column="1", sticky="e")
input_filename = Entry(f1, textvariable = filenameInput)
input_filename.grid(row="10", column="2", sticky="w")
#line 11
Label(f1, text=" ").grid(row="11", column="0")
#line 12
Radiobutton(f1, text="Blank Node", variable=v, value=3, command = blank).grid(row=12, column=1, sticky="w")
#line 13
Label(f1, text="Create a blank node and add any text you want to it").grid(row="13", column="1", columnspan="6", sticky="w")
#line 14
blankNode = Label(f1, text="[Currently 1 Row, 1 Column]", textvariable = blankNodeValue).grid(row="14", column="1", columnspan="3", sticky="n")
#line 15
Label(f1, text="1   Columns    2  ").grid(row="15", column="2", sticky="w")
#line 16
Label(f1, text="1").grid(row="16", column="1", sticky="e")
Radiobutton(f1, text="", variable=rc, value=1, command = blank).grid(row=16, column=2, sticky="w")
Radiobutton(f1, text="", variable=rc, value=6, command = blank).grid(row=16, column=2, sticky="n")
#line 17
Label(f1, text="2").grid(row="17", column="1", sticky="e")
Radiobutton(f1, text="", variable=rc, value=2, command = blank).grid(row=17, column=2, sticky="w")
Radiobutton(f1, text="", variable=rc, value=7, command = blank).grid(row=17, column=2, sticky="n")
#line 18
Label(f1, text="Rows 3").grid(row="18", column="1", sticky="e")
#Label(f1, text="3").grid(row="18", column="1", sticky="e")
Radiobutton(f1, text="", variable=rc, value=3, command = blank).grid(row=18, column=2, sticky="w")
Radiobutton(f1, text="", variable=rc, value=8, command = blank).grid(row=18, column=2, sticky="n")
#line 19
Label(f1, text="4").grid(row="19", column="1", sticky="e")
Radiobutton(f1, text="", variable=rc, value=4, command = blank).grid(row=19, column=2, sticky="w")
Radiobutton(f1, text="", variable=rc, value=9, command = blank).grid(row=19, column=2, sticky="n")
#line 20
Label(f1, text="5").grid(row="20", column="1", sticky="e")
Radiobutton(f1, text="", variable=rc, value=5, command = blank).grid(row=20, column=2, sticky="w")
Radiobutton(f1, text="", variable=rc, value=10, command = blank).grid(row=20, column=2, sticky="n")
#line 21
Label(f1, text=" ").grid(row="21", column="0")
#line 22

def next():
	print(v.get())
	print(rc.get())
	print(filenameInput.get())
	raise_frame(f2)


#Button(f1, text='Next >', command=lambda:raise_frame(f2)).grid(row="22", column="4", sticky="W")
Button(f1, text='Cancel', command=lambda:root.destroy()).grid(row="22", column="2", sticky="S")
Button(f1, text='Next >', command=next).grid(row="22", column="3", sticky="W")

#line 0
Label(f2, text="           ").grid(row="0", column="0")
Label(f2, text="           ").grid(row="0", column="1")
Label(f2, text="           ").grid(row="0", column="2")
Label(f2, text="           ").grid(row="0", column="3")
Label(f2, text="           ").grid(row="0", column="4")
Label(f2, text="           ").grid(row="0", column="5")
Label(f2, text="           ").grid(row="0", column="6")
Label(f2, text="           ").grid(row="0", column="7")
#line 1
Label(f2, text="           Project ViP - GUI").grid(row="1", column="2")
Label(f2, text="V0.7").grid(row="1", column="4")
#line 2
Label(f2, text=" ").grid(row="2", column="0", sticky="N, W")
#line 3
Label(f2, text=" Please choose an output type;").grid(row="3", column="1", sticky="W", columnspan="3")
#line 4
Label(f2, text=" ").grid(row="4", column="0")
#line 5
Radiobutton(f2, text="Compact", variable=ot, value=1, command = outputType).grid(row="5", column="1", sticky="w", columnspan=2) 
#line 6
Label(f2, text="Both the base and the text / Braille sections are printed").grid(row="6", column="1", columnspan=5, sticky="w")
#line 7
Label(f2, text="as one object.").grid(row="7", column="1", columnspan=5, sticky="w")
#line 8
Radiobutton(f2, text="Exploded", variable=ot, value=2, command = outputType).grid(row="8", column="1", sticky="w", columnspan=2) 
#line 9
Label(f2, text="Only the text / Braille sections are printed.").grid(row="9", column="1", columnspan=5, sticky="w")
#line 10
Label(f2, text="The base is not produced.").grid(row="10", column="1", columnspan=5, sticky="w")
#line 11
Radiobutton(f2, text="Exploded + Lego", variable=ot, value=3, command = outputType).grid(row="11", column="1", sticky="w", columnspan=2) 
#line 12
Label(f2, text="Both the base and the text / Braille sections are printed").grid(row="12", column="1", columnspan=5, sticky="w")
#line 13
Label(f2, text="with Lego connectors to join them together.").grid(row="13", column="1", columnspan=5, sticky="w")
#line 14
Label(f2, text=" ").grid(row="14", column="0")
#line 15
Label(f2, text="Filename : ").grid(row="15", column="1", sticky="e")
input_filename = Entry(f2, textvariable = filenameOutput)
input_filename.grid(row="15", column="2", sticky="w")
#line 16
Label(f2, text=" ").grid(row="16", column="0")
#line 17
Label(f2, text=" ").grid(row="17", column="0")
#line 18
Label(f2, text=" ").grid(row="18", column="0")
#line 19
Label(f2, text=" ").grid(row="19", column="0")
#line 20
Label(f2, text=" ").grid(row="20", column="0")
#line 21
Label(f2, text=" ").grid(row="21", column="0")
#line 22
Button(f2, text='< Back', command=lambda:raise_frame(f1)).grid(row="22", column="1", sticky="W")
Button(f2, text='Cancel', command=lambda:root.destroy()).grid(row="22", column="2", sticky="S")
Button(f2, text='Next >', command=lambda:raise_frame(f3)).grid(row="22", column="3", sticky="W")


#line 0
Label(f3, text="           ").grid(row="0", column="0")
Label(f3, text="           ").grid(row="0", column="1")
Label(f3, text="           ").grid(row="0", column="2")
Label(f3, text="           ").grid(row="0", column="3")
Label(f3, text="           ").grid(row="0", column="4")
Label(f3, text="           ").grid(row="0", column="5")
Label(f3, text="           ").grid(row="0", column="6")
Label(f3, text="           ").grid(row="0", column="7")
#line 1
Label(f3, text="           Project ViP - GUI").grid(row="1", column="2")
Label(f3, text="V0.7").grid(row="1", column="4")
#line 2
Label(f3, text=" ").grid(row="2", column="0", sticky="N, W")
#line 3
Label(f3, text="Here we go....;").grid(row="3", column="1", sticky="W", columnspan="3")
#line 4
Label(f3, text=" ").grid(row="4", column="0")


def runIt():
	print(filenameInput.get())
	print(filenameOutput.get())
	print(rc.get())
	print(v.get())
	print(ot.get())


Button(f3, text='< Back', command=lambda:raise_frame(f1)).grid(row="22", column="1", sticky="W")
Button(f3, text='Cancel', command=lambda:root.destroy()).grid(row="22", column="2", sticky="N")
Button(f3, text='Run', command=runIt).grid(row="22", column="3", sticky="W")

raise_frame(f1)
root.mainloop()
