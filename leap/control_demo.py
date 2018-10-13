import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import sys, pygame
from pygame.locals import *

#from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def main():
    pygame.init()

    size = width,height = 640,480

    backg = 180,216,233

    screen = pygame.display.set_mode(size)

    pod = pygame.image.load("tide-pod.png")
    podrect = pod.get_rect()
    podrect.center = (width/2, height/2)

    controller = Leap.Controller()
    print(controller.devices)
    old_pos = (width/2, height/2)
    while not(controller.is_connected):
        pass
    
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_r] or pygame.key.get_pressed()[K_SPACE]:
                    podrect.center = (width/2, height/2)
            #pass
        if(controller.is_connected):
            frame = controller.frame()
            hand = frame.hands[0]
            #print (hand.palm_velocity)
            
            #get velocity for pod
            speed = (hand.palm_velocity[0]/200,-hand.palm_velocity[1]/200)

            depth = (hand.palm_position[2])

            rotate = hand.direction.roll
            #move ball
            podrect = podrect.move(speed)
            
        else: print("not connected")

        
        screen.fill(backg)
        screen.blit(pod, podrect)
        pygame.display.flip()        
        
if __name__ == "__main__":
    main()
