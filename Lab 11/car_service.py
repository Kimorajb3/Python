import tkinter

class AutoServices:

    def __init__(self, parent):
        self.main_window = parent

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.OCcost = tkinter.IntVar()
        self.LJcost = tkinter.IntVar()
        self.RFcost = tkinter.IntVar()
        self.TFcost = tkinter.IntVar()
        self.Icost = tkinter.IntVar()
        self.MRcost = tkinter.IntVar()
        self.TRcost = tkinter.IntVar()

        self.OCbutton = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00',variable = self.OCcost, onvalue = 30)
        self.LJbutton = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable = self.LJcost, onvalue = 20)
        self.RFbutton = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable = self.RFcost, onvalue = 40)
        self.TFbutton = tkinter.Checkbutton(self.top_frame, text='Transmission Flush - $100.00', variable = self.TFcost, onvalue = 100)
        self.Ibutton = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable = self.Icost, onvalue = 35)
        self.MRbutton = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable = self.MRcost, onvalue = 200)
        self.TRbutton = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable = self.TRcost, onvalue = 20)

        self.total_button = tkinter.Button(self.bottom_frame, text = 'Display Charges', command = self.do_something)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.charges = tkinter.Label(self.middle_frame, text='$0.00')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        self.OCbutton.pack()
        self.LJbutton.pack()
        self.RFbutton.pack()
        self.TFbutton.pack()
        self.Ibutton.pack()
        self.MRbutton.pack()
        self.TRbutton.pack()

        self.total_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.charges.pack(side='left')

    def do_something(self):
        self.charges.config(text="${}.00".format(sum(map(tkinter.IntVar.get, [self.OCcost, self.LJcost, self.RFcost, self.TFcost, self.Icost, self.MRcost, self.TRcost]))))

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = AutoServices(root)
    root.mainloop()
        

