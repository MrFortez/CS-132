from tkinter import (
    # Widgets 
    Frame, Label, Text, PhotoImage, Entry,

    # Constants
    X, Y, BOTH,
    BOTTOM, RIGHT, LEFT,
    DISABLED, NORMAL, END,

    # Type Hint Stuff
    Tk 
)
from room import Room
import os 

class Game(Frame):

    # some constants
    EXIT_ACTION = ["quit", "exit", "bye", "adios"]
    WIDTH = 800
    HEIGHT = 600

    # statuses
    class Status:
        DEFAULT = "I don't understand. Try [verb noun]. Valid verbs are go, look, take, and use."
        DEAD = "You are dead. Not big suprise"
        BAD_EXIT = "Invalid Exit"
        ROOM_CHANGED = "Room Changed"
        GRABBED = "Item Grabbed"
        BAD_GRABBABLE = "I can't grab that"
        BAD_ITEM = "I don't see that"

    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.inventory = []
        self.pack(fill=BOTH, expand=1) # geometry managment for game instances

    def setupGame(self) -> None:
        
        # create the rooms
        r1 = Room("Room 1", os.path.join("images", "room1.gif"))
        r2 = Room("Room 2", os.path.join("images", "room2.gif"))
        r3 = Room("Room 3", os.path.join("images", "room3.gif"))
        r4 = Room("Room 4", os.path.join("images", "room4.gif"))

        # create exits
        r1.addExit("east", r2)
        r1.addExit("south", r3)

        r2.addExit("west", r1)
        r2.addExit("south", r4)
        
        r3.addExit("east", r4)
        r3.addExit("north", r1)
    
        r4.addExit("west", r3)
        r4.addExit("north", r2)
        r4.addExit("south", None)
        
        # add items
        r1.addItem("chair", "It's made of wicker.")
        r1.addItem("big_table", "It's made of wicker but bigger.")

        r2.addItem("dog", "it is made of wicker")
        r2.addItem("wicker", "it is made of wicker")

        r3.addItem("tooth", "It's made of wicker")
        r3.addItem("floor", "It's made of wicker")

        r4.addItem("dwayne_the_rock_johnson", "He imade of pure muscle.")
        r4.addItem("diva", "It's made of wicker")

        # add grabbables
        r1.addGrabbable("key")

        r2.addGrabbable("baby_gronk")

        r3.addGrabbable("The_Ultimate_Godly_Legendary_Super_Saiyan_True_Excalibur")

        r4.addGrabbable("a_gun")

        # set current room
        self.current_room = r1

    def setupGUI(self) -> None:
        
        # the input element
        self.playerInput = Entry(self, bg="white", fg="black")
        self.playerInput.bind("<Return>", self.processInput)
        self.playerInput.pack(side=BOTTOM, fill=X)
        self.playerInput.focus()

        # the image element
        img = None
        imgWidth = Game.WIDTH // 2
        self.imageContainer = Label(
            self,
            width=imgWidth,
            image=img
        )
        self.imageContainer.image = img
        self.imageContainer.pack(side=LEFT, fill=Y)
        self.imageContainer.pack_propagate(False)

        # the info area
        textContainerWidth = Game.WIDTH // 2
        textContainer = Frame(self, width=textContainerWidth)
        self.text = Text(
            textContainer,
            bg="lightgrey",
            fg="black",
            state=DISABLED
        )
        self.text.pack(fill=Y, expand=1)
        textContainer.pack(side=RIGHT, fill=Y)
        textContainer.pack_propagate(False)
        

    def setImage(self):
        pass

    def setStatus(self, status: str):
        pass
    
    def clearEntry(self):
        pass

    def handleGo(self, direction):
        pass

    def handleLook(self, item):
        pass

    def handleTake(self, grabbable):
        pass

    def handleUse(self, event):
        pass

    def handleDefault(self, event):
        pass

    def play(self):
        pass

    def processInput(self):
        pass