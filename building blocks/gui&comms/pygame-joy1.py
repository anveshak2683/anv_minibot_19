import pygame,thread,sys
from _thread import * 
import socket
import time


#from termcolor import colored

class Run():
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        start_new_thread( self.joyEvent,())

        host = '127.0.0.1'
        port = 10005
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            self.s.bind((host,port))
            print ("Waiting for connection...")
        except socket.error as e:
            print(str(e))
        self.s.listen(1)
        

    def joyEvent(self):
        while True:
            for event in pygame.event.get():
                pass
            try:
                self.joystick.init()
            except Exception:
                print ("[ERROR] initializing joystick!!") ; sys.exit(0)

            self.x =self.joystick.get_button(0)
            self.y = self.joystick.get_axis(2)
            self.p = self.joystick.get_axis(1)
            

    def spin(self):
        while True:
            conn,addr = self.s.accept()
            print ('Got Connection from', addr)
            while True:
                try:
                    conn.send(b'%d  %f  %g'%(self.x,self.y,self.p))
                    time.sleep(0.5)
                except :
                    
                    break
            conn.close()
            
			

if __name__ == '__main__':
        

        run = Run()
        run.spin()
