import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import pygame

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    pygame.init()
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    def on_init(self, controller):
        print("Initialized")
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_connect(self, controller):
        print ("Connected")


    def on_disconnect(self, controller):
        print ("OI! Where'd it go?")

    def on_exit(self, controller):
        print  ("All doneeeeeeeee...")

    def send_commands(self, frame):
        

    def on_frame(self, controller):
        frame = controller.frame()
        #Get Hands
        for hand in frame.hands:
            print (hand.palm_position)
        send_commands(frame)
            
        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                print ("  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        gesture.id, self.state_names[gesture.state],
                        circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness))

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                print ("  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                        gesture.id, self.state_names[gesture.state],
                        swipe.position, swipe.direction, swipe.speed))

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                print ("  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        keytap.position, keytap.direction ))

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                print ("  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        screentap.position, screentap.direction ))

    
                
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return ("STATE_START")

        if state == Leap.Gesture.STATE_UPDATE:
            return ("STATE_UPDATE")

        if state == Leap.Gesture.STATE_STOP:
            return ("STATE_STOP")

        if state == Leap.Gesture.STATE_INVALID:
            return ("STATE_INVALID")


def main():
    
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
