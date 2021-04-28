from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
import sys

root = Tk()
root.title('Sorting Graphs')
root.maxsize(1375, 600)
root.config(bg='#323232')

#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 1300
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 6
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['blue' for x in range(len(data))])

def StartAlgorithm():
    global data
    bubble_sort(data, drawData, 0.01)


def exit():
    sys.exit()


#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='turquoise')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1350, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]

Button(UI_frame, text="Start", command=StartAlgorithm, bg='#33ff33').grid(row=1, column=1, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=100, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=0, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=0, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=0, padx=5, pady=5)
Button(UI_frame, text="Exit", command=exit, bg='white').grid(row=1, column=2, padx=5, pady=5)



root.mainloop()

