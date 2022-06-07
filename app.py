import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import PyPDF2
from PIL import Image, ImageTk
import cv2
import os
root = tk.Tk()  # starting of the windows

canvas = tk.Canvas(root, width=500, height=200)
canvas.grid(columnspan=3, rowspan=2)

# logo
logo = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions

instructions = tk.Label(root, text="\nCapture button below\n", font="Raleway", fg='blue')
instructions.grid(columnspan=3, column=0, row=1)


def video_capturing():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    human_cascade = cv2.CascadeClassifier('fullbody.xml')

    out = cv2.VideoWriter(
        'output.avi',
        cv2.VideoWriter_fourcc(*'MJPG'),
        8,
        (640, 480))
    while True:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        humans = human_cascade.detectMultiScale(gray, 1.9, 1)
        # humans = human_cascade.detectMultiScale(gray, 1.4, 2)
        rectangle = None
        for (x, y, w, h) in humans:
            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print(rectangle)
        cv2.imshow('frame', frame)
        # print(detecing)
        if rectangle is not None:
            out.write(frame.astype('uint8'))

        elif rectangle is None:
            # key = cv2.waitKey(0)
            # if key % 256 == 1:
            #     break
            print("Video is not detected")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Browse button
browse_text = tk.StringVar()
click_button = Image.open("final.png")
root.click_buttton = ImageTk.PhotoImage(click_button)

def on_enter(event):
    button.config(image=root.click_buttton)


button = tk.Button(root, image=root.click_buttton, bg='white', bd=0, command=lambda: video_capturing())

canvas.create_window(10, 5, window=button)
button.grid(column=1, row=2)

# button = tk.Button(root, textvariable=browse_text, command=lambda: video_capturing(), font="Raleway", bg="#20bebe",
#                    fg="white", width=15, height=2, borderwidth=10)
#
# browse_text.set("Open")
# button.grid(column=1, row=2)

canvas = tk.Canvas(root, width=400, height=50)
canvas.grid(columnspan=3)

root.mainloop()  # ending of the windows
