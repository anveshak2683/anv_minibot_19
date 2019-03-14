import pygame,thread,sys
from termcolor import colored

class Run():
	def __init__(self):
		pygame.init()
		pygame.joystick.init()

		self.joystick = pygame.joystick.Joystick(0)
		thread.start_new_thread( self.joyEvent,())

	def joyEvent(self):
		while True:
			for event in pygame.event.get():
				pass
			try:
				joystick.init()
			except Exception:
				print "[ERROR] initializing joystick!!"; sys.exit(0)
			x = joystick.get_button(2)
			y = joystick.get_axis(1)

	def spin(self):
		while True:
			#Send data to run motor
			pass

if __name__ == '__main__':
	run = Run()
	run.spin()
