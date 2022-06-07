from tkinter import *
import tkinter as tk
master = tk.Tk()
bgimg= tk.PhotoImage(file="D:\\Pycharm Projects\\Camera_Detection\\logo.png")
#Specify the file name present in the same directory or else
#specify the proper path for retrieving the image to set it as background image.
limg= Label(master, image=bgimg)
limg.pack()
master.mainloop()