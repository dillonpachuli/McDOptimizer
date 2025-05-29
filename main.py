from tkinter import *
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = Tk()

root.title("McDonalds Optimizer")
root.geometry('350x200')

root.mainloop()