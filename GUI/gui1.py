
from tkinter import *
from tkinter.ttk import *

root = Tk()

class App():
    def __init__(self):
        root.geometry("500x430")

        root.configure(bg='#ececec')

        self.input_widget()
        self.output_widget()
        self.blank_widget()
        self.run_widget()

    def input_widget(self):
        label_input = Label(root, text="Input").grid(row="0")
        list_input = ["Clipboard", "Blank", "test"]
        self.var_input = StringVar()
        self.var_input.set(list_input[0]) # default value
        drop_input = OptionMenu(root, self.var_input, *list_input).grid(row="0", column="1")


    def clipboard_widget(self):
        cliptext = root.clipboard_get()
        label_clip = Label(root, text = cliptext).grid(row="0", column="2")

    def blank11(self):
        print("11")

    def blank12(self):
        print("12")

    def blank_widget(self):
        label_input = Label(root, text="Columns").grid(row="5")

        v = IntVar()
        Radiobutton(root, text="1 Line 1 Column", variable=v, value=1, command = self.blank11).grid(row=6, column=1) 
        Radiobutton(root, text="1 Line 2 Column", variable=v, value=2, command = self.blank12).grid(row=6, column=2)
        
    def output_widget(self):
        label_output = Label(root, text="Output Type").grid(row="1")
        list_output = ["Compact","Exploded","Exploded Lego"] #read in folder which contains the output types in then when a new one is created it will be added to the list
        var_output = StringVar()
        var_output.set(list_output[0]) # default value
        drop_output = OptionMenu(root, var_output, *list_output).grid(row="1", column="1")

    def runHit(self):
        print("value is", self.var_input.get())
        #master.quit()

    def run_widget(self):
            button_run = Button(root, text="Run", command=self.runHit).grid(row="2", column="1") #runs the program based on the output method chosen, and reads in the input choice



        
class Run():
    app = App()

if __name__ == "__main__":
    root.mainloop()

