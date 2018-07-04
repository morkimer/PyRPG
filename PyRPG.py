# this is a test
hp, mhp = 10, 10
x, y, z = 0, 0, 0

def main():
	define_rooms()
	print("\nPyRPG\nby Chris Shoeman (morkimer).\nhttps://github.com/morkimer/PyRPG\nThis is my first Python project, and I am learning Python on the fly as I write the code. If there is anything I can do to improve the code, feel free to submit an issue on the Issues page on Github or submit a pull request.\n\nYour health is ",hp,"/",mhp,".\n")
	getRoom()
	while True:
		get_input()

def get_input():
	cmd = input(">")
	if cmd in ["north", "south", "west", "east", "up", "down"]:
		move(cmd)
	elif cmd == "exit" or cmd == "quit":
		exit()
	else:
		print("Unknown command.")

def move(direction):
	global x
	global y
	global z
	global rooms
	for r in rooms:
		if direction == "north":
			if r.exitN == True:
				z += 1
			else:
				print("You cannot move there.")
			getRoom()
		elif direction == "west":
			if r.exitW == True:
				x -= 1
			else:
				print("You cannot move there.")
			getRoom()
		elif direction == "south":
			if r.exitS == True:
				z -= 1
			else:
				print("You cannot move there.")
			getRoom()
		elif direction == "east":
			if r.exitE == True:
				x += 1
			else:
				print("You cannot move there.")
			getRoom()
		elif direction == "up":
			if r.exitU == True:
				y += 1
			else:
				print("You cannot move there.")
			getRoom()
		elif direction == "down":
			if r.exitD == True:
				y -= 1
			else:
				print("You cannot move there.")
			getRoom()

def getRoom():
	global rooms
	global x
	global y
	global z
	for r in rooms:
		if r.cx == x and r.cy == y and r.cz == z:
			print(r.name," ("+ str(x) +","+ str(y) +","+ str(z) +")\n",r.desc,"\n")

class room:
	def __init__(self, name, desc, cx, cy, cz, exitN, exitW, exitS, exitE, exitU, exitD, items):
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
		self.items = items

def define_rooms():
	global rooms
	rooms = [
		room("Test Room", "Lorem ipsum dolor sit amet...", 0, 0, 0, False, False, False, False, False, True, []),
		room("Test Basement", "This is the basement of the test room.", 0, -1, 0, False, False, False, False, True, False, [])
		]


















# do not move this, keep at bottom
main()
