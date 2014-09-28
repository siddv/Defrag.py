import random
import launchpad
from pygame import time

btnToggle = []

LP = launchpad.Launchpad()
LP.Open()
LP.Reset()

def main():

	global posY

	reset()

	while 1:
		# If defrag emulation is on rows up to and including 8
		if posY[0] <= 8: 

			# 90% chance to progress normally.
			if random.randint(0,10) > 1: 
				progress() 

			# 10% chance of a burst run.
			else: 
				burst()

		# Reset when gets to row 9.
		else:
			reset()

		# Reset if lowermost circular button is pressed.
		btn = LP.ButtonStateRaw()
		if btn != []: 
			if btn[0] == 120 and btn[1] == True:
				reset()


def reset():

	global posX
	global posY
	global colour
	global delay


	# Position Vars. Three; One for each state: off, red and green.
	posX = [0,0,0]							
	posY = [1,1,1]

	# Color and delay set. Three for each state again.
	colour = [[0,0],[3,0],[0,3]]
	delay = [[10,1500],[10,1500],[0,0]]
	
	# Turn all LEDs orange
	LP.LedAllOn();

	# Short loop to turn the circular buttons off
	for x in range(0, 9):
		LP.LedCtrlXY(x, 0, 0, 0)
		LP.LedCtrlXY(8, x, 0, 0)

		
def progress():

	global posX
	global posY
	global colour
	global delay

	# Progress by a random number between 2 and 6 blocks
	progression = random.randint(2,6)

	# Run 3 times, one for each state.
	for x in range(0, 3):

		for y in range(0, progression):

			# If progression has reached the 8th column, increase the row number and reset the column number.
			if posX[x] == 8:
				posY[x] += 1
				posX[x] = 0

			# Set LED Colours according to the state and colour var in setup.
			LP.LedCtrlXY(posX[x], posY[x], colour[x][0], colour[x][1])

			# Increase column number.
			posX[x] = posX[x]+1

		# Wait a rancom number of milliseconds according to the delay var.
		time.wait(random.randint(delay[x][0],delay[x][1]))


def burst():

	global posX
	global posY
	global colour
	global delay

	progression = random.randint(5,8)

	for y in range(0, progression):

		for x in range(0, 3):

			if posX[x] == 8:
				posY[x] += 1
				posX[x] = 0

			LP.LedCtrlXY(posX[x], posY[x], colour[x][0], colour[x][1])

			posX[x] = posX[x]+1

			time.wait(100)


if __name__ == '__main__':
	main()

