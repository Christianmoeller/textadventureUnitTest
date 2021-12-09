import tkinter as tk
from tkinter import font
from tkinter.constants import W

window = tk.Tk() # Erstelle ein Object der Klasse TK namnes window

windowMinWidth = 400
windowMinHeight = 400

windowMaxWidth = 800
windowMaxHeight = 800


#Funktionen die den Output Regeln
def calcForPrudentium():
    outputVariable = inputFeld.get()
    try:
        outputVariable = int(outputVariable)

        outputVariable *= 4
        outputLable = tk.Label(master=outputFrame, text="Du brauchst "+str(outputVariable)+" Inferium Essenzen", font=("Arial", 20))
        outputLable.pack()
    except ValueError:
        print("Bitte Zahleingeben")

def calForTertium():
    outputVariable = inputFeld.get()
    try:
        outputVariable = int(outputVariable)

        outputVariable *= 16
        outputLable = tk.Label(master=outputFrame, text="Du brauchst "+str(outputVariable)+" Inferium Essenzen", font=("Arial", 20))
        outputLable.pack()
    except ValueError:
        print("Bitte Zahleingeben")

def calcForImperium():
    outputVariable = inputFeld.get()
    try:
        outputVariable = int(outputVariable)

        outputVariable *= 64
        outputLable = tk.Label(master=outputFrame, text="Du brauchst "+str(outputVariable)+" Inferium Essenzen", font=("Arial", 20))
        outputLable.pack()
    except ValueError:
        print("Bitte Zahleingeben")

def calcForSupremium():
    outputVariable = inputFeld.get()
    try:
        outputVariable = int(outputVariable)

        outputVariable *= 256
        outputLable = tk.Label(master=outputFrame, text="Du brauchst "+str(outputVariable)+" Inferium Essenzen", font=("Arial", 20))
        outputLable.pack()
    except ValueError:
        print("Bitte Zahleingeben")

    pylolo = 0
def calcForInsanium():
    outputVariable = inputFeld.get()
    try:
        outputVariable = int(outputVariable)

        outputVariable *= 1024
        outputLable = tk.Label(master=outputFrame, text="Du brauchst "+str(outputVariable)+" Inferium Essenzen", font=("Arial", 20))
        outputLable.pack()
    except ValueError:
        print("Bitte Zahleingeben")

window.minsize(windowMinWidth, windowMinHeight)
window.maxsize(windowMaxWidth, windowMaxHeight)

#Erstelle Frames um auf diesen Frames zu arbeiten
headlineFrame = tk.Frame()
inputFrame = tk.Frame()
buttonFrame = tk.Frame()
outputFrame = tk.Frame()
deletFrame = tk.Frame()

#Headline
programmName = tk.Label(master=headlineFrame, text="Mystical Agriculture Calculator", font=("Arial", 20))
programmName.pack()

#Inputfeld für den User um zu sagen weieviele er haben will

inputFeld = tk.Entry(master=inputFrame)
inputFeldDeffinition = tk.Label(master=inputFrame, text="Wieviele willst du haben?", font=("Arial", 15))


inputFeldDeffinition.grid(row=1, column=0)
inputFeld.grid(row=1, column=1)

#Buttons für jede Art der Essenz

buttonPrudentium = tk.Button(master=buttonFrame,text="Prudentium", command=calcForPrudentium)
buttonTertium = tk.Button(master=buttonFrame, text="Tertium", command=calForTertium)
buttonImperium = tk.Button(master=buttonFrame,text="Imperium", command=calcForImperium)
buttonSupremium = tk.Button(master=buttonFrame,text="Supremium", command=calcForSupremium)
buttonInsanium = tk.Button(master=buttonFrame,text="Insanium", command=calcForInsanium)

buttonPrudentium.grid(row=0,column=0)
buttonTertium.grid(row=0, column=1)
buttonImperium.grid(row=0, column=2)
buttonSupremium.grid(row=0, column=3)
buttonInsanium.grid(row=0, column=4)

#delete Button
buttonDelete = tk.Button(master=deletFrame, text="Delete")
buttonDelete.pack()

#Textfeld des Ergenbises


headlineFrame.pack()
inputFrame.pack()
buttonFrame.pack()
outputFrame.pack()
deletFrame.pack()
window.mainloop() # Lässt die Application laufen 