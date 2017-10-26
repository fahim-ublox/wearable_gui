import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()


        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='nsew')

        self.labelVariable = Tkinter.StringVar()
        self.label2Variable = Tkinter.StringVar()


        label = Tkinter.Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=2,sticky='nsew')

        label2 = Tkinter.Label(self,textvariable=self.label2Variable, anchor="w",fg="white",bg="black")
        label2.grid(column=0,row=2,columnspan=2,sticky='nsew')

        self.labelVariable.set("You clicked the button !")
        self.label2Variable.set("I will be the greatest software developer on the surface of earth")

        #self.grid_columnconfigure(0,weight=1)

        #self.grid_rowconfigure(0, weight=1)
        self.resizable(False,False)



        


if __name__ == "__main__":

    #read_file()
    app = simpleapp_tk(None)
    app.geometry("256x128")
    app.mainloop()
