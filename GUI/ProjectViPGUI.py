from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror 
import subprocess as sub
import os.path


import time   # temp


def raise_frame(frame):
	frame.tkraise()
	
def load_file():
	fname = askopenfilename(title="Select input file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
	if fname:
		try:
			print(fname)
		except:                     # <- naked except is a bad idea
			showerror("Open Source File", "Failed to read file\n'%s'" % fname)
		return fname

def load_directory():
	fname = askdirectory(title="Select target folder")
	if fname:
		try:
			print(fname)
		except:                     # <- naked except is a bad idea
			showerror("Open Source File", "Failed to read file\n'%s'" % fname)
		return fname
	
def getInputFilename():
	fn = load_file()	
	filenameInput.set(fn)
	v.set(2)	

def getOutputFilename():
	fn = load_directory()	
	filenameOutput.set(fn)

def clipboard():
	get_clipboard()
	v.set(1)
	print("clipboard selected")

def filename_selected():
	print("filename selected")
	v.set(2)
	
def filename(fn):
	print("filename : " + fn.get())	
	v.set(2)

def filenameOut(fn):
	print("filename out : " + fn.get())	

def blank():
	print("blank")
	v.set(3)
	blankNodeValue.set(" ")
#	blankNodeValue.set(getBlankDesc(rc))

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

clipboard_text = ""
def get_clipboard():
	try:
		clipboard_text = root.clipboard_get()
	except:
		print("Clipboard Empty")
	print("Clipboard text : " + clipboard_text)

s = Style()
s.configure('My.TFrame', background='#ececec')

f1 = Frame(root, style='My.TFrame')
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
# which input option is selected
v = IntVar()
v.set(1)
# which blank option is selected
rc = IntVar()
rc.set(1)
r1c1t = IntVar()
r1c2t = IntVar()
r2c1t = IntVar()
r2c2t = IntVar()
r3c1t = IntVar()
r3c2t = IntVar()
r4c1t = IntVar()
r4c2t = IntVar()
r5c1t = IntVar()
r5c2t = IntVar()

r1c1e = StringVar()
r1c2e = StringVar()
r2c1e = StringVar()
r2c2e = StringVar()
r3c1e = StringVar()
r3c2e = StringVar()
r4c1e = StringVar()
r4c2e = StringVar()
r5c1e = StringVar()
r5c2e = StringVar()
blankTitle = StringVar()

# filename input
filenameInput = StringVar()
filenameInput.trace("w", lambda name, index, mode, sv=filenameInput: filename(filenameInput))
# output type
ot = IntVar()
ot.set(1)
# filename output
filenameOutput = StringVar()
filenameOutput.trace("w", lambda name, index, mode, sv=filenameOutput: filenameOut(filenameOutput))

def blankName(field):
	print(field)
	v.set(3)

#blank field values
r1c1e.trace("w", lambda name, index, mode, sv=r1c1e: blankName(r1c1e))
r1c2e.trace("w", lambda name, index, mode, sv=r1c2e: blankName(r1c2e))
r2c1e.trace("w", lambda name, index, mode, sv=r2c1e: blankName(r2c1e))
r2c2e.trace("w", lambda name, index, mode, sv=r2c2e: blankName(r2c2e))
r3c1e.trace("w", lambda name, index, mode, sv=r3c1e: blankName(r3c1e))
r3c2e.trace("w", lambda name, index, mode, sv=r3c2e: blankName(r3c2e))
r4c1e.trace("w", lambda name, index, mode, sv=r4c1e: blankName(r4c1e))
r4c2e.trace("w", lambda name, index, mode, sv=r4c2e: blankName(r4c2e))
r5c1e.trace("w", lambda name, index, mode, sv=r5c1e: blankName(r5c1e))
r5c2e.trace("w", lambda name, index, mode, sv=r5c2e: blankName(r5c2e))


blankNodeValue = StringVar()
blankNodeValue.set(" ")
#blankNodeValue.set(getBlankDesc(rc))

for frame in (f1, f2, f3, f4):
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
Label(f1, text="        Project ViP - GUI              v0.8").grid(row="1", column="0", columnspan=7)

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
Radiobutton(f1, text="File", variable=v, value=2, command = filename_selected).grid(row="9", column="1", sticky="w") 
#line 10
Label(f1, text="Filename : ").grid(row="10", column="1", sticky="e")
input_filename = Entry(f1, textvariable = filenameInput)
input_filename.grid(row="10", column="2", sticky="w")
Button(f1, text='Browse', command=getInputFilename).grid(row="10", column="3")
#line 11
Label(f1, text=" ").grid(row="11", column="0")
#line 12
Radiobutton(f1, text="Blank Node", variable=v, value=3, command = blank).grid(row=12, column=1, sticky="w")
#line 13



titleFrame = Frame(f1)
titleFrame.grid(row=13, column=0, columnspan=6)

Label(titleFrame, text="Title : ").grid(row=0, column=0, sticky="w")
title = Entry(titleFrame, textvariable =blankTitle)
title.grid(row=0, column=1, sticky="w")

#line 14


blankFrame = Frame(f1)
blankFrame.grid(row=16, column=0, columnspan=6)

#line 15
Label(blankFrame, text=" E").grid(row="0", column="1", sticky="w") 
Label(blankFrame, text=" D").grid(row="0", column="2", sticky="w") 
Label(blankFrame, text="Text").grid(row="0", column="3", sticky="n") 
Label(blankFrame, text="Text").grid(row="0", column="4", sticky="n") 
Label(blankFrame, text=" E").grid(row="0", column="5", sticky="w") 
Label(blankFrame, text=" D").grid(row="0", column="6", sticky="n")

#line 16
Radiobutton(blankFrame, text="", variable=r1c1t, value=1, command = blank).grid(row=1, column=1, sticky="w")
Radiobutton(blankFrame, text="", variable=r1c1t, value=2, command = blank).grid(row=1, column=2, sticky="e")
r1c1 = Entry(blankFrame, textvariable =r1c1e)
r1c1.grid(row=1, column=3, sticky="w")
r1c2 = Entry(blankFrame, textvariable =r1c2e)
r1c2.grid(row=1, column=4, sticky="w")
Radiobutton(blankFrame, text="", variable=r1c2t, value=1, command = blank).grid(row=1, column=5, sticky="n")
Radiobutton(blankFrame, text="", variable=r1c2t, value=2, command = blank).grid(row=1, column=6, sticky="n")

#line 17
Radiobutton(blankFrame, text="", variable=r2c1t, value=1, command = blank).grid(row=2, column=1, sticky="w")
Radiobutton(blankFrame, text="", variable=r2c1t, value=2, command = blank).grid(row=2, column=2, sticky="e")
r2c1 = Entry(blankFrame, textvariable =r2c1e)
r2c1.grid(row=2, column=3, sticky="w")
r2c2 = Entry(blankFrame, textvariable =r2c2e)
r2c2.grid(row=2, column=4, sticky="w")
Radiobutton(blankFrame, text="", variable=r2c2t, value=1, command = blank).grid(row=2, column=5, sticky="n")
Radiobutton(blankFrame, text="", variable=r2c2t, value=2, command = blank).grid(row=2, column=6, sticky="n")

#line 17
Radiobutton(blankFrame, text="", variable=r3c1t, value=1, command = blank).grid(row=3, column=1, sticky="w")
Radiobutton(blankFrame, text="", variable=r3c1t, value=2, command = blank).grid(row=3, column=2, sticky="e")
r3c1 = Entry(blankFrame, textvariable =r3c1e)
r3c1.grid(row=3, column=3, sticky="w")
r3c2 = Entry(blankFrame, textvariable =r3c2e)
r3c2.grid(row=3, column=4, sticky="w")
Radiobutton(blankFrame, text="", variable=r3c2t, value=1, command = blank).grid(row=3, column=5, sticky="n")
Radiobutton(blankFrame, text="", variable=r3c2t, value=2, command = blank).grid(row=3, column=6, sticky="n")

#line 17
Radiobutton(blankFrame, text="", variable=r4c1t, value=1, command = blank).grid(row=4, column=1, sticky="w")
Radiobutton(blankFrame, text="", variable=r4c1t, value=2, command = blank).grid(row=4, column=2, sticky="e")
r4c1 = Entry(blankFrame, textvariable =r4c1e)
r4c1.grid(row=4, column=3, sticky="w")
r4c2 = Entry(blankFrame, textvariable =r4c2e)
r4c2.grid(row=4, column=4, sticky="w")
Radiobutton(blankFrame, text="", variable=r4c2t, value=1, command = blank).grid(row=4, column=5, sticky="n")
Radiobutton(blankFrame, text="", variable=r4c2t, value=2, command = blank).grid(row=4, column=6, sticky="n")

#line 17
Radiobutton(blankFrame, text="", variable=r5c1t, value=1, command = blank).grid(row=5, column=1, sticky="w")
Radiobutton(blankFrame, text="", variable=r5c1t, value=2, command = blank).grid(row=5, column=2, sticky="e")
r5c1 = Entry(blankFrame, textvariable =r5c1e)
r5c1.grid(row=5, column=3, sticky="w")
r5c2 = Entry(blankFrame, textvariable =r5c2e)
r5c2.grid(row=5, column=4, sticky="w")
Radiobutton(blankFrame, text="", variable=r5c2t, value=1, command = blank).grid(row=5, column=5, sticky="n")
Radiobutton(blankFrame, text="", variable=r5c2t, value=2, command = blank).grid(row=5, column=6, sticky="n")


#blankNode = Label(f1, text="[Currently 1 Row, 1 Column]", textvariable = blankNodeValue).grid(row="21", column="1", columnspan="3", sticky="n")
blankNode = Label(f1, text=" ", textvariable = blankNodeValue).grid(row="21", column="1", columnspan="3", sticky="n")




#line 21
Label(f1, text=" ").grid(row="22", column="0")
#line 22

def next():
	print(v.get())
	print(rc.get())
	print(filenameInput.get())
	raise_frame(f2)

buttonframe1 = Frame(f1)
buttonframe1.grid(row=22, column=1, columnspan=3)    
Button(buttonframe1, text='< Prev',state="disabled", command=lambda:raise_frame(f2)).grid(row="0", column="0", sticky="NSEW")
Button(buttonframe1, text='Cancel', command=lambda:root.destroy()).grid(row="0", column="1", sticky="NSEW")
Button(buttonframe1, text='Next >', command=next).grid(row="0", column="2", sticky="NSEW")

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
Label(f2, text="Project ViP - GUI              v0.8").grid(row="1", column="0", columnspan=7)
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
Label(f2, text="Output Folder Name : ").grid(row="15", column="1", sticky="e")
input_filename = Entry(f2, textvariable = filenameOutput)
input_filename.grid(row="15", column="2", sticky="w")
Button(f2, text='Browse', command=getOutputFilename).grid(row="15", column="3")

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


def update_frame3():

	# line 4
	if v.get() == 1:
		Label(f3, text="Clipboard").grid(row="4", column="2")
	elif v.get() == 2:
		Label(f3, text=filenameInput.get()).grid(row="4", column="2", columnspan="7", sticky="w")
	else:
		rows = 1
		cols = rc.get()
		if rc.get() > 4:
			cols = rc.get() - 4
			row = 2
		Label(f3, text="Blank node : " + str(rows) + " rows, " + str(cols) + " columns.").grid(row="4", column="2", columnspan=6, sticky="w")
	#line 7
	Label(f3, text=filenameOutput.get()).grid(row="7", column="2", columnspan="7", sticky="w")
	
	#line 10
	if ot.get() == 1:
		Label(f3, text="Compact").grid(row="10", column="2", columnspan=3, sticky="w")
	elif ot.get() == 2:
		Label(f3, text="Exploded").grid(row="10", column="2", columnspan=3, sticky="w")
	else:
		Label(f3, text="Exploded, with Lego connetors").grid(row="10", column="2", columnspan=3, sticky="w")
		
	raise_frame(f3)


	
buttonframe2 = Frame(f2)
buttonframe2.grid(row=22, column=1, columnspan=3) 		
#line 22
Button(buttonframe2, text='< Back', command=lambda:raise_frame(f1)).grid(row="0", column="0", sticky="NSEW")
Button(buttonframe2, text='Cancel', command=lambda:root.destroy()).grid(row="0", column="1", sticky="NSEW")
Button(buttonframe2, text='Next >', command=update_frame3).grid(row="0", column="2", sticky="NSEW")		

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
Label(f3, text="          Project ViP - GUI              v0.8").grid(row="1", column="0", columnspan=7)
#line 2
Label(f3, text=" ").grid(row="2", column="0", sticky="N, W")
#line 3
Label(f3, text="Input from;").grid(row="3", column="1", sticky="e")
#line 4

	
#line 5
Label(f3, text=" ").grid(row="5", column="0")
#line 6
Label(f3, text="Output to;").grid(row="6", column="1", sticky="e")
#line 7

#line 8
Label(f3, text=" ").grid(row="8", column="0")
#line 9
Label(f3, text="Node type;").grid(row="9", column="1", sticky="e")
#line 10

for c in range(10,22):
	Label(f3, text=" ").grid(row=c, column="0")


		
def getDataPin(pinType):
	if (pinType.get() != None):
		if (pinType.get() == 1):
			return "exec"
		elif pinType.get() == 2:
			return "data"
		else:
			return pinType.get()

def runIt():
	raise_frame(f4)
	print(filenameInput.get())
	print(filenameOutput.get())
	print(rc.get())   # blank type
	print(v.get())    # input option
	print(ot.get())   # output type
	
#	txt.insert("end", filenameInput.get()+ "\n")
#	txt.see("end")	
	outputType = "?"
	if ot.get() == 1:
		outputType = "Compact"
	elif ot.get() == 2:
		outputType = "Exploded"
	else:
		outputType = "ExplodedLego"
	
	inputFile = "?"	
	if v.get() == 1:   # clipboard
		clipboard_text = root.clipboard_get()
		print(str(len(clipboard_text)) + " bytes read from clipboard")
		file = open("clipboard", "w")
		inputFile = os.path.abspath("clipboard")
		file.write(clipboard_text)
		file.close()
		command = ["python","./InvokeExtractNodes.py", outputType, inputFile, filenameOutput.get()]
	elif v.get() == 2:  # file
		inputFile = filenameInput.get()
		command = ["python","./InvokeExtractNodes.py", outputType, inputFile, filenameOutput.get()]
	else:    # blank
		print(blankTitle.get())
		print(str(r1c1t.get()) + ":" + r1c1.get() + "   " + r1c2.get() + ":" + str(r1c1t.get()))
		print(str(r2c1t.get()) + ":" + r2c1.get() + "   " + r2c2.get() + ":" + str(r2c2t.get()))
		print(str(r3c1t.get()) + ":" + r3c1.get() + "   " + r3c2.get() + ":" + str(r3c2t.get()))
		print(str(r4c1t.get()) + ":" + r4c1.get() + "   " + r4c2.get() + ":" + str(r4c2t.get()))
		print(str(r5c1t.get()) + ":" + r5c1.get() + "   " + r5c2.get() + ":" + str(r5c2t.get()))
		####

		ivars = [r1c1t, r1c1, r1c2t, r1c2, r2c1t, r2c1, r2c2t, r2c2, r3c1t, r3c1, r3c2t, r3c2, r4c1t, r4c1, r4c2t, r4c2,
		 r5c1t, r5c1, r5c2t, r5c2]
		command = ["python3","./genBlank.py", filenameOutput.get(), outputType, blankTitle.get()]

		while True:
			for t in ivars:
				x = getDataPin(t)
				if x == 0:
					break
				else:
					command.append(x)
			break		
		
		print(command)


#		sys.exit(0)
	
#	command = ["python","./InvokeExtractNodes.py", outputType, inputFile, filenameOutput.get()]
	p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
	output, errors = p.communicate()
	txt.insert("end", output)
	txt.insert("end", "===============> Any Errors Follow <================")
	txt.insert("end", errors)
	txt.see("end")
	
buttonframe3 = Frame(f3)
buttonframe3.grid(row=22, column=1, columnspan=4) 

Button(buttonframe3, text='< Back', command=lambda:raise_frame(f2)).grid(row="0", column="1", sticky="NSEW")
Button(buttonframe3, text='Cancel', command=lambda:root.destroy()).grid(row="0", column="2", sticky="NSEW")
Button(buttonframe3, text='Run', command=runIt).grid(row="0", column="3", sticky="NSEW")	

    # create a Text widget
txt = Text(f4, borderwidth=3, height=22, width=65, relief="sunken")
txt.config(font=("consolas", 12), undo=True, wrap='word')
txt.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
scrollby = Scrollbar(f4, command=txt.yview)
scrollby.grid(row=1, column=1, sticky='nsew')
txt['yscrollcommand'] = scrollby.set


buttonframe4 = Frame(f4)
buttonframe4.grid(row=22, column=0, columnspan=2) 

Button(buttonframe4, text='< Back', command=lambda:raise_frame(f3)).grid(row="0", column="1", sticky="NSEW")
Button(buttonframe4, text='Cancel', command=lambda:root.destroy()).grid(row="0", column="2", sticky="NSEW")
Button(buttonframe4, text='      ',state="disabled", command=runIt).grid(row="0", column="3", sticky="NSEW")




raise_frame(f1)
root.mainloop()
