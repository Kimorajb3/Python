import tkinter

class Mygui:
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.info = tkinter.StringVar()
        self.showInfo = tkinter.Label(self.top_frame, textvariable = self.info)
        
        
        self.show_button = tkinter.Button(self.bottom_frame, text = 'Show Info', command = self.do_something)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.showInfo.pack()
        self.show_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_something(self):
        self.info.set('Steven Marcus\n274 Bailey Drive\nWaynesville, NC 27999')

do_something = Mygui()
