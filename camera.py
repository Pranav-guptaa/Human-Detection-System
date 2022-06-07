import tkinter as tk
import cv2

from IPython.terminal.pt_inputhooks import tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.grid(column=1, row=0)


def capture_video():
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

root.mainloop()