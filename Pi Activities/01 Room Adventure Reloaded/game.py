########################################################
# Brandon Fortes, Blair Borque, Adam Guillory
########################################################

import random
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
    WIDTH = 2000
    HEIGHT = 1500

    # statuses
    class Status:
        DEFAULT = "I don't understand. Try [verb noun]. Valid verbs are go, look, take, use, unlock, eat, and place."
        DEAD = "You are dead. Not big suprise. The house exploded all around you, shattering the diamond into tons of shards. It was a pretty gruesome death ngl. \n But hey, at least you died doing what you loved: being smothered by a big diamond"
        BAD_EXIT = "Invalid Exit"
        ROOM_CHANGED = "Room Changed"
        GRABBED = "Item Grabbed"
        BAD_GRABBABLE = "I can't grab that"
        BAD_ITEM = "I don't see that"
        BAD_UNLOCK = "There's nothing to unlock"

    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.inventory = []
        self.pack(fill=BOTH, expand=1) # geometry managment for game instances

    def setupGame(self) -> None:

        # Names for each room, used to determing which items get put where
        roomTypes = [["Bathroom", "Bedroom", "Dining Room"], ["Game Room", "Kitchen", "Laundry Room"], ["Living Room", "Office", "Storage Room"]]

        self.turnCount = 0 # increments each time the player makes an input.
        self.escapeTurnCount = 0 # increments each time the player makes an input in escape.

        #randomize the safe's code
        global safeCode 
        safeCode = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
        print(safeCode) #For debuging purposes
        
        #randomize the vault's code
        global vaultCode
        vaultCode = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
        print(vaultCode) #For debuging purposes

        #determine the color order for the vault code
        global vaultCodeOrder
        vaultCodeOrder = ["red", "yellow", "green", "blue", "purple"]
        random.shuffle(vaultCodeOrder)

        # array of rooms
        roomLayout = [[None, None, None], [None, None, None], [None, None, None]]
            
        # create the rooms, assigning each room a roomType
        for i in range(0,3):
            for j in range(0, 3):
                roomLayout[i][j] = Room(roomTypes[i][j], os.path.join("images", f"{roomTypes[i][j]}.gif"))

        # randomize room layout
        random.shuffle(roomLayout)

        #this room is for the end sequence and will be attached to a random viable room
        global escapeRoom; escapeRoom = Room("Escape", os.path.join("images", "win.gif"))

        #this room will hold the vault, and will be attached to a bottom or middle row room as a down exit
        global vaultRoom; vaultRoom = Room("Vault", os.path.join("images", "Vault.gif"))

        # Booleans for when in the safe or vault unlocking process (because tkinter is dumb and stupid)
        self.isUnlockingSafe = False
        self.isUnlockingVault = False
        
        #add the exits
        for i in range(0,3):
            for j in range(0, 3):
                if i > 0:
                    roomLayout[i][j].addExit("north", roomLayout[i - 1][j])
            
                if j < 2:
                    roomLayout[i][j].addExit("east", roomLayout[i][j + 1])
    
                if i < 2:
                    roomLayout[i][j].addExit("south", roomLayout[i + 1][j])

                if j > 0:
                    roomLayout[i][j].addExit("west", roomLayout[i][j - 1])

        #the exit room will be attached to any room in the top row, always as a north exit
        exitLocation = random.randint(0, 2)
        roomLayout[0][exitLocation].addItem("door", "a door in the north of this room. that seems to lead out of the mansion. It is barricaded, you'd need some kind of tool to break through")
        roomLayout[0][exitLocation].addExit("north", escapeRoom)

    
        #Vault will always be in one of the bottom 3 rooms
        vaultLocation = [random.randint(1, 2), random.randint(0, 2)]  
        roomLayout[vaultLocation[0]][vaultLocation[1]].addItem("rug", "an extravagant rug on the floor. You decided to look under it, miraculously finding a trapdoor leading to the basement to the mansion. It looks like there are three key holes on the door, a red one, a blue one, and a green one. I Bet whatever's down here is worth a ton!")
        roomLayout[vaultLocation[0]][vaultLocation[1]].addExit("down", vaultRoom)
        vaultRoom.addExit("up", roomLayout[vaultLocation[0]][vaultLocation[1]])
        vaultRoom.addItem("vault", "A massive circular vault on the wall. It stands between you and your beautiful treasure. For some strange reason, you feel as if you're going to need to have seen five different colored squares in order to solve this.")
        
        
        # # add items and grabbables based on the room type
        for row in roomLayout:
            for room in row:
                match room.name:
                    case "Bathroom":
                        room.addItem("sink", "A sink. It is quite the exquisite display of craftmanship. You are very tempted to use the sink...")
                        room.addItem("bathtub", "A bathtub / shower hybrid. You consider taking a shower, but you decide against it. Too much work")
                        room.addItem("toilet", "A toilet. What a wonderful creation. On a closer inspection you realize that theres no flush handle on it, how unfortunate.")
                    case "Bedroom":
                        room.addItem("bed", f"A queen-sized bed, it's quite comfortable. You look under the sheets and find a yellow slip of paper with the number {vaultCode[vaultCodeOrder.index('yellow')]} on it!")
                        room.addItem("bedstand", "A small table next to the bed.")
                        room.addItem("closet", "A large closet on the side of the room. Suprisingly, you find nothing of value in here.")
                        room.addGrabbable("flashlight", "bedstand")

                    case "Dining Room":
                        room.addItem("chair", "A wooden chair. Or is it? Is it Really a chair if every interaction that the chair is capable of being a part of is explained by the atoms that make it up? There is nothing for the existence of a chair to explain. Saying that chair exists is like saying that two books are three objects: a book; the other book; and the two books. It is needlessly overcounting the amount of objects actually present in that space. In reality, there is no chair there, and there was never a chair there. There are only a mass of atoms arranged into a form that we foolishly claim is a chair and that is an object over and above the atoms it is made of")
                        room.addItem("steak", "A medium rare steak on a glass plate, sitting next to a glass of wine and a proper formation of forks and knives next to it. Fancy family, huh? You are getting pretty hungry though, and that steak looks very eatable")

                    case "Game Room":
                        room.addItem("pooltable", "An old pool table.")
                        room.addItem("dartboard", f"A dart board. There are darts on {safeCode[0]}, {safeCode[1]}, and {safeCode[2]}")
                        room.addGrabbable("8ball", "pooltable")

                    case "Kitchen": 
                        room.addItem("stove","A cooking stove.")
                        room.addItem("refrigerator", "A black refrigerator.")
                        room.addGrabbable("apple", "refrigerator")

                    case "Laundry Room":
                        room.addItem("washer", "A washing machine full of clothes. You consider taking their Vsauce tshirt, but you decide against it. It is simply too powerful.")
                        room.addItem("dryer", "A dryer not full of clothes. In fact, there's nothing inside. Theres also nothing outside, because there never was a dryer, there never was a washing machine, there never was a laundry room. This is all a dream... wake up... \n just kidding.")

                    case "Living Room":
                        room.addItem("coffee_table", "a monsterous concoction that is, in fact, made of wicker")
                        room.addItem("mantle", "A brick mantle with a fireplace")
                        room.addItem("plant", "A large potted plant in the corner. It has shriveled due to a lack of light")

                    case "Office":
                        room.addItem("stapler", "that is one of the staplers of all time")
                        room.addItem("hole_punch", "a hole puncher, great for punching holes.")
                        room.addItem("drawer", "a drawer in the office desk. It has quite the exquisite handle, huh? Finely crafted by the Ancient Egyptians out of pure wicker. Truly a mastercraft of design and craftmanship. You feel an immensly strong urge to open it.")

                    case "Storage Room":
                        room.addItem("toolbox", "a toolbox with an assortment of tools. ")
                        room.addGrabbable("crowbar", "toolbox")
                        room.addGrabbable("screwdriver", "toolbox")
                        room.addItem("cardboard_box", "A cardboard box. You look inside and see a vast array of random junk, and by a vast array I mean one screw and thats it.")
        

        # add general items and grabbables
        roomLayout[random.randint(0, 2)][random.randint(0, 1)].addItem("safe", "A metal safe with a 3 digit lock (use the verb unlock to try and solve it)")
        roomLayout[random.randint(0, 2)][random.randint(0, 2)].addItem("cage", "a small bird cage. Theres a lock with a black spherical hole in it. If only you had a black spherical object to place in it")
        roomLayout[random.randint(0, 2)][random.randint(0, 2)].addItem("clock", "an old grandfather clock. Looks like it has a few loose screws. There may be a way to get inside")
       
        keyLocation = random.randint(0, 2)
        roomLayout[0][keyLocation].addItem("table","A woooden table.")
        roomLayout[0][keyLocation].addGrabbable("key","table")
        


        #set Locks
        roomLayout[random.randint(1, 2)][random.randint(0, 2)].isLocked = True
        vaultRoom.isLocked = True
        escapeRoom.isLocked = True
        
        # set current room
        self.currentRoom = roomLayout[0][0]

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
        self.imageContainer.pack(side=LEFT, fill=BOTH)
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
        if (self.currentRoom == None):
            img = PhotoImage(file=os.path.join("images", "skull.gif"))
        else:
            img = PhotoImage(file=self.currentRoom.image)

        self.imageContainer.config(image=img)
        self.imageContainer.image = img

    def setStatus(self, status: str):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)

        if self.currentRoom == None:
            self.text.insert(END, Game.Status.DEAD)
        else:
            content = f"{self.currentRoom}\n"
            content += f"You are carrying: {self.inventory}\n\n"
            content += status

            if ("big_diamond" in self.inventory and not self.currentRoom.name == "Escape"):
                content += f"\n You have {10 - self.escapeTurnCount} turns left"

            self.text.insert(END, content)

        self.text.config(state=DISABLED)        

    def clearEntry(self):
        self.playerInput.delete(0, END)

    def removeItemFromInventory(self, noun):
        for i in range(0, len(self.inventory)):
            if (self.inventory[i] == noun):
                self.inventory.pop(i)
                break


    def handleGo(self, direction):
        status = Game.Status.BAD_EXIT

        if direction in self.currentRoom.exits:
            if (self.currentRoom.exits[direction].isLocked):
                status = "That room is locked"
            else:
                self.currentRoom = self.currentRoom.exits[direction]
                status = Game.Status.ROOM_CHANGED

        self.setStatus(status)
        self.setImage()

    def handleLook(self, item):
        status = Game.Status.BAD_ITEM
        if item in self.currentRoom.items:
            status = self.currentRoom.items[item]
            for grabbable in self.currentRoom.grabbables:
                if (grabbable[1] == item):
                    status +=  " There is a " + grabbable[0] + " in it. "

        self.setStatus(status)

    def handleTake(self, item):
        status = Game.Status.BAD_GRABBABLE

        for grabbable in self.currentRoom.grabbables:
            if (item == grabbable[0]):
                self.inventory.append(grabbable[0])
                self.currentRoom.deleteGrabbable(grabbable)
                status = grabbable[0]
        
        self.setStatus(status)

    def handleUse(self, item):
        response = "That item doesnt exist"

        # Use functions for items
        for object in self.currentRoom.items:
            if (object == item):
                if (item == "sink"):
                    if (not "blue_key" in self.inventory):
                        response = "You turned on the sink. Water begins to flow into the bowl. You watch it for a while, what a beautiful sight. As you watch it, a blue key begins to materialize from the water. Seeing this, you snap out of your trance, grab it, and turn off the water"
                        self.inventory.append("blue_key")
                    else:
                        response = "You have already turned the sink on. That is an experience you can only have once in your life. Cherish it. Your eagerness to partake in this experience again demonstrates humanity's unending desire for pleasure and consumption. For Shame."

                if (item == "steak"):
                    if (not "red_key" in self.inventory):
                        response = "You take a moment to sit down at the table, place your cloth on your lap, and start slowly eating the steak. It tastes fantastic, clearly these guys had some master chefs. While enjoying the steak, you bite on someething really hard. A bone maybe? You take a look and its a red key! You put it to the side and finish the steak, then you take it and move on."
                        self.inventory.append("red_key")
                    else: 
                        response = "As much as it hurts, you hold back your eagerness to consume the steak, as alas... the steak was already consumed. "
               
                if (item == "drawer"):
                    if (not "green_key" in self.inventory):
                        response = "You take your chance, grip the handle, and open the drawer. Inside, you find... another drawer? You open that one too, and find yet another drawer. You open it, another drawer. Again? Yep, another drawer. Drawers upon drawers until finally, you find a green key. You spend the next 10 minutes closing all of the drawers so that it doesn't look suspicious."
                        self.inventory.append("green_key")
                    else: 
                        response = "Opening that drawer was a trap you vowed to never fall for again..."

                

        # Use functions for grabbables
        for object in self.inventory:
            if (object == item):
                response = "That item cannot be used here"
                if (item == "key"):
                    response = "There are no locked doors in this rooom"
                    for room in self.currentRoom.exits.values():
                        if (room.isLocked and (not room.name == "Escape") and (not room.name == "Vault")):
                            room.isLocked = False
                            self.removeItemFromInventory(item)
                            response = f"You unlocked the doors to {room.name}"
                            break

                elif (item == "blue_key" or item == "green_key" or item == "red_key"):
                    if ("down" in self.currentRoom.exits):
                        response = "In order to use the colored keys to open the trapdoor, use phrase unlock trapdoor"

                    else:
                        response = "There doesnt seem to be anything that fits this key. If you do find something, use verb unlock"

                elif (item == "apple"):
                    response = f"You took a bite out of the apple. You found a slip of blue paper with the number {vaultCode[vaultCodeOrder.index('blue')]} on it inside!"

                elif (item == "screwdriver"):
                    response = "Theres nothing to use a screwdriver on here"
                    if ("clock" in self.currentRoom.items):
                        response = f"You used the screwdriver to unscrew the loose screws, inside you found a green slip of paper with the number {vaultCode[vaultCodeOrder.index('green')]} on it inside! \nYou screw everything back into place so theres no trace left"

                elif (item == "8ball"):
                    response = "The 8 ball doesnt seem to have any use in this room"
                    if ("cage" in self.currentRoom.items):
                        response = f"You placed the 8 ball into the lock's sphereical hole, causing the cage door to swing open. In the cage you found a red slip of paper with the number {vaultCode[vaultCodeOrder.index('red')]} on it! \n Afterwards you close the cage"

                elif (item == "flashlight"):
                    response = "You turned on the flashlight and aimed it all around the room. Nothing happened"
                    if ("plant" in self.currentRoom.items):
                        response = f"You turned on the flashlight and aimed it all around the room. When you aimed it at the plant its leaves suddenly unfurrled and revealed a purple slip of paper with the number {vaultCode[vaultCodeOrder.index('purple')]} on it inside! \n The plant then shrivels back to its sad state"

                elif (item == "crowbar"):
                    response = "theres nothing important to break in this room"
                    if ("door" in self.currentRoom.items):
                        response = "You smashed the barricades on the door, the exit is now open!"
                        escapeRoom.isLocked = False

                elif (item == "white_paper"):
                    response = "You look at the white paper again. It has 5 squares: "
                    for color in vaultCodeOrder:
                        response += "a " + color + " square. " 



        self.setStatus(response)

    def handleUnlock(self, event):
        response = Game.Status.BAD_UNLOCK

        if (event == "safe" and "safe" in self.currentRoom.items):
            if (not "white_paper" in self.inventory):
                response = "input a 3 digit code"
                self.isUnlockingSafe = True
            else:
                response = "You already unlocked the safe."
        

        if (event == "trapdoor" and "rug" in self.currentRoom.items):
            response = "It seems like you dont have all three keys. Go look around the mansion more"
            if ("blue_key" in self.inventory and "green_key" in self.inventory and "red_key" in self.inventory):
                response = "You used all three keys on the trapdoor, unlocking it."
                vaultRoom.isLocked = False
        

        if (event == "vault" and "vault" in self.currentRoom.items):
            if (not "big_diamond" in self.inventory):
                response = "input a 5 digit code"
                self.isUnlockingVault = True
            else:
                response = "You already unlocked the vault. Why are you trying the building is about to explode!!!"

        self.setStatus(response)


    def handleDefault(self, event):
        self.setStatus(Game.Status.DEFAULT)
        self.clearEntry()

        # If the player made an invalid input, dont increment the turn count (by just subtracting one)
        self.turnCount -= 1
        if ("big_diamond" in self.inventory):
            self.escapeTurnCount -= 1

    def play(self):
        self.setupGame()
        self.setupGUI()
        self.setImage()
        self.setStatus("")

    def processInput(self, event):

        # get the input from the entry element
        action = self.playerInput.get()
        action = action.lower()

        # stop the game if applicable
        if (action in Game.EXIT_ACTION):
            exit()

        # increment turn count
        self.turnCount += 1

        # increment turn count in escape
        if ("big_diamond" in self.inventory):
            self.escapeTurnCount += 1
    
        # Handle the Safe unlocking process because tkinter is the worst program ever written
        if (self.isUnlockingSafe):
            self.isUnlockingSafe = False
            inputCode = action
            if (len(inputCode) == 3):
                if (inputCode[0] == str(safeCode[0]) and inputCode[1] == str(safeCode[1]) and inputCode[2] == str(safeCode[2])):
                    response = "Correct Code! The safe unlocked, revealing a white slip of paper with five squares:  \n"
                    for color in vaultCodeOrder:
                        response += "a " + color + " square. " 
                    response += "You take the slip of paper with you (if you want to look at it again, do use white_paper)"
                    self.inventory.append("white_paper")
                else:
                    response = "Incorrect Code (if you would like to try again, do unlock safe again)"

            else:
                response = "Invalid Code. Use the format 123, with no spaces between the numbers (if you would like to try again, do unlock safe again)"
            self.setStatus(response)
            self.clearEntry()
            return
        
        # Handle the Vault unlocking process because tkinter is the worst program ever written
        if (self.isUnlockingVault):
            self.isUnlockingVault = False
            inputCode = action
            if (len(inputCode) == 5):
                if (inputCode[0] == str(vaultCode[0]) and inputCode[1] == str(vaultCode[1]) and inputCode[2] == str(vaultCode[2]) and inputCode[3] == str(vaultCode[3]) and inputCode[4] == str(vaultCode[4])):
                    response = 'Correct Code! The vault unlocked! Inside you found a giant diamond!:  \nSoon afterwards, an incredibly loud alarm began to play \n "UNAUTHORIZED PERSON HAS OPENED VAULT, SELF DESTRUCTING IN 10 MINUTES" \nLooks like its time to find a way out!'
                    self.inventory.append("big_diamond")
                else:
                    response = "Incorrect Code (if you would like to try again, do unlock vault again)"

            else:
                response = "Invalid Code. Use the format 12345, with no spaces between the numbers (if you would like to try again, do unlock vault again)"
            self.setStatus(response)
            self.clearEntry()
            return

        # sanitize the input
        words = action.split()

        # handle an incorrect syntax input
        if len(words) != 2:
            self.handleDefault(action)
            return
        
        # assign verbs and nouns
        verb = words[0]
        noun = words[1]

        # handle input
        match verb:
            case "go":
                self.handleGo(noun)
            case "look":
                self.handleLook(noun)
            case "take":
                self.handleTake(noun)
            case "use":
                self.handleUse(noun)
            case "unlock":
                self.handleUnlock(noun)

            # These next few will serve as proxys for the Use function (if you wanted to you could say "use steak", but thats weird)
            case "eat":
                self.handleUse(noun) 
            case "place":
                self.handleUse(noun)
            case "open":
                self.handleUse(noun)

            # Default
            case _:
                self.handleDefault("")

         # If player enters the escapeRoom, they win*
        if (self.currentRoom.name == "Escape"):
            print("[poggers]")
            if ("big_diamond" in self.inventory):
                self.setStatus(f"You managed to escape, and with the big diamond in tow! You walk out of the mansion in style, not looking at the explosion happening behind you because you are the coolest person to ever live. Time to buy 3000 mcdonalds chicken nuggets! \n You did it in {self.turnCount} turns.")
            else:
                self.setStatus(f"You managed to escape, but you didnt find much of value. You walk out of the mansion with a solemn expression, dreaming about the things you wish you had. Oh well :/ \n You did it in {self.turnCount} turns.")
            return

        # Player loses if they spend too long in escape
        print(self.escapeTurnCount)
        if (self.escapeTurnCount > 9):
            self.currentRoom = None
            print("Bad at the game ngl")

        # clear the entry if the current room is None
        if (self.currentRoom == None):
            self.clearEntry()
            self.setImage()
            self.setStatus("L")
            return

        print(self.currentRoom)
        self.clearEntry()
            