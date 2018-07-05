# This is the source code for PyRPG! Feel free to modify as you please.
# Originally written by Chris Shoeman (morkimer)
# https://github.com/morkimer/PyRPG

hp, mhp, lvl, xp, mxp = 10, 10, 1, 0, 100
gld = 0
x, y, z = 0, 0, 0

def main():
    define_rooms()
    print("\nPyRPG\nby Chris Shoeman (morkimer).\nhttps://github.com/morkimer/PyRPG\nThis is my first Python project, and I am learning Python on the fly as I write the code. If there is anything I can do to improve the code, feel free to submit an issue on the Issues page on Github or submit a pull request.\n\nYou have "+str(hp)+"/"+str(mhp)+" HP.\n")
    while True:
        getRoom()
        get_input()

def get_input():
    cmd = input(">")
    if cmd in ["north", "south", "west", "east", "up", "down"]:
        move(cmd)
    elif cmd == "exit" or cmd == "quit":
        exit()
    elif cmd == "help":
        print("\nPyRPG Commands\n")
        print("HELP      Shows this help")
        print("GO        Moves in the direction you type (NORTH, SOUTH, EAST, WEST, UP, DOWN)")
        print("QUIT      Quits out of the game")
        print("LOOK      Look around the room (shows the room description)")
        print("INV       Shows items in your inventory")
        print("INSPECT   Examine an item in your inventory")
        print("TAKE      Takes an item")
        print("DROP      Drops an item")
        print("SAY       Say something")
        print("\nIf you need more detailed help, type ""help <COMMAND>"".")
    elif cmd == "look":
        for r in rooms:
            if r.cx == x and r.cy == y and r.cz == z:
                print(r.name," ("+ str(x) +","+ str(y) +","+ str(z) +")\n",r.desc,"\n")
    elif cmd == "inventory" or cmd == "inv":
        if inventory != []:
            itemlist = "Items in inventory: "
            itemstring = ""
            for a in inventory:
                if itemstring == "":
                    itemstring = str(a.name)
                else:
                    itemstring = itemstring,str(a.name)
            print(itemlist + str(itemstring) + "\n")
        else:
            print("You have nothing in your inventory.\n")
    else:
        if len(cmd.split()) > 0:
            cmdwords = cmd.split()
            if cmdwords[0] == "help":
                print("\nPyRPG Commands\n")
                if cmdwords[1] == "go":
                    print('GO\nMoves you in any of six directions, if there is a room in that direction.\n\nExample: go north\nThis will add 1 to your Y coordinate and place you in the room at your updated coordinates. If there is a wall blocking your way, it will say:\n  You cannot move there.\n\nYou can omit the "go" portion of the command and just type the direction (ex. "west").\n')
                elif cmdwords[1] == "quit":
                    print('QUIT\nQuits out of the game and either closes the window/instance of Python or returns to the interpreter.\n\nExample: quit\n\nYou can also type "exit" if you feel like typing that.\n')
                elif cmdwords[1] == "look":
                    print('LOOK\nAll it does is show the description of the room again.\n')
                elif cmdwords[1] == "inv":
                    print('INV\nDisplays the contents of your inventory. If, for example, you have a Sandwich in your inventory, it will print:\n\n  Items in inventory: ("Sandwich")\n\nIf you want to (for some inexplicable reason), you can type "inventory" as well.\n')
                elif cmdwords[1] == "inspect":
                    print('INSPECT\nViews all the details of a specified item in your inventory.\n')
#                elif cmdwords[1] == "":
#                    print('\n\n')
            if cmdwords[0] == "say":
                saystring = " ".join(cmdwords[1:])
                print('You said "' + saystring + '".')
            elif cmdwords[0] == "take":
                for r in rooms:
                    if r.cx == x and r.cy == y and r.cz == z:
                        if r.items != []:
                            for a in r.items:
                                saystring = " ".join(cmdwords[1:])
                                if saystring == a.name:
                                    inventory.append(a)
                                    r.items.remove(a)
                                    print("You took " + str(a.name) + ".")
            elif cmdwords[0] == "drop":
                for r in rooms:
                    if r.cx == x and r.cy == y and r.cz == z:
                        if inventory != []:
                            for a in inventory:
                                saystring = " ".join(cmdwords[1:])
                                if saystring == a.name:
                                    r.items.append(a)
                                    inventory.remove(a)
                                    print("You dropped " + str(a.name) + ".")
            elif cmdwords[0] == "inspect":
                    if inventory != []:
                        for a in inventory:
                            saystring = " ".join(cmdwords[1:])
                            if saystring == a.name:
                                print("Inspecting "+a.name+"...\nItem type: "+a.itype+"\nRequires level "+str(a.level)+"\nDescription: "+a.desc+"\nAttributes: "+str(a.attributes))
            else:
                print("Unknown command.")
        else:
            print("Unknown command.")

def move(direction):
    global x
    global y
    global z
    global rooms
    for r in rooms:
        if r.cx == x and r.cy == y and r.cz == z:
            if direction == "north":
                if r.exitN == True:
                    z += 1
                else:
                    print("You cannot move there.")
            elif direction == "west":
                if r.exitW == True:
                    x -= 1
                else:
                    print("You cannot move there.")
            elif direction == "south":
                if r.exitS == True:
                    z -= 1
                else:
                    print("You cannot move there.")
            elif direction == "east":
                if r.exitE == True:
                    x += 1
                else:
                    print("You cannot move there.")
            elif direction == "up":
                if r.exitU == True:
                    y += 1
                else:
                    print("You cannot move there.")
            elif direction == "down":
                if r.exitD == True:
                    y -= 1
                else:
                    print("You cannot move there.")
            break

def getRoom():
    global rooms
    global x
    global y
    global z
    for r in rooms:
        if r.cx == x and r.cy == y and r.cz == z:
            if r.hasVisited != True:
                r.hasVisited = True
                print(r.name," ("+ str(x) +","+ str(y) +","+ str(z) +")\n",r.desc,"\n")
            else:
                print(r.name," ("+ str(x) +","+ str(y) +","+ str(z) +")\n")
            if r.items != []:
                itemlist = "Items in room: "
                itemstring = ""
                for a in r.items:
                    if itemstring == "":
                        itemstring = str(a.name)
                    else:
                        itemstring = itemstring,str(a.name)
                print(itemlist + str(itemstring) + "\n")

class room:
    def __init__(self, name, desc, cx, cy, cz, exitN, exitW, exitS, exitE, exitU, exitD, hasVisited, items):
        self.name = name
        self.desc = desc
        self.cx = cx
        self.cy = cy
        self.cz = cz
        self.exitN = exitN
        self.exitW = exitW
        self.exitS = exitS
        self.exitE = exitE
        self.exitU = exitU
        self.exitD = exitD
        self.hasVisited = hasVisited
        self.items = items
class item:
    def __init__(self, name, desc, level, itype, attributes):
        self.name = name
        self.desc = desc
        self.level = level
        self.itype = itype
        self.attributes = attributes
class attr:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

def define_rooms():
    global rooms
    rooms = [
        room("Test Room", "Lorem ipsum dolor sit amet...", 0, 0, 0, False, True, False, False, False, True, False, []),
        room("Test Basement", "This is the basement of the test room.", 0, -1, 0, False, False, False, False, True, False, False, []),
        room("Test Hallway", "Wow! You can access rooms here.", -1, 0, 0, True, True, True, True, True, False, False, []),
        room("Test Living Room", "There is stuff here.", -2, 0, 0, True, False, False, True, False, False, False, []),
        room("Test Kitchen", "Food was prepared here.", -2, 0, 1, False, False, True, False, False, False, False, [item("Sandwich", "Restores 5 HP", 0, "food", [attr("heal",5)])]),
        room("Test Bathroom", "Stuff.", -1, 0, 1, False, False, True, False, False, False, False, []),
        room("Test Closet", "You are in the closet of the Test House.", -1, 0, -1, True, False, False, False, False, False, False, [item("Worn Hiking Boots", "These boots seem to have had some heavy use through the years...", 1, "armor", [attr("defc",1)])])
        ]






# do not move this, keep at bottom
inventory = []
main()
