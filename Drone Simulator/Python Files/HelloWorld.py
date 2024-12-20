# In this example, drone will takeoff, move forward for 2 seconds and then land.
from codrone_simulator import Drone
from codrone_simulator import Note
import time

drone = Drone()
drone.pair() # Controller will pair with Drone in Simulator

# Executed Commands
drone.takeoff() # Drone will take off from stationary

drone.hover(2) # Drone will hover in the air for 2 seconds

# "A, B, C Song, Play Buzzer sounds
drone.drone_buzzer(Note.C4, 1000)  # A
time.sleep(0.1)
drone.drone_buzzer(Note.C4, 1000)  # B
time.sleep(0.1)
drone.drone_buzzer(Note.G4, 1000)  # C
time.sleep(0.1)

drone.hover(2) # Drone will hover in the air for 2 seconds

drone.land() # Drone will Land 


drone.close() # Drone closes Communication