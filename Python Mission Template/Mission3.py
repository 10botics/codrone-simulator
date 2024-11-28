from codrone_simulator import Drone
from codrone_simulator import Note
import time

# Initialize and pair with the drone
drone = Drone()
drone.pair()

# Mission 3 task execution
drone.takeoff()

# Play a melody using the drone buzzer
drone.drone_buzzer(Note.C4, 300)  # Play C4 for 300ms
time.sleep(0.1)
drone.drone_buzzer(Note.D4, 300)  # Play D4 for 300ms
time.sleep(0.1)
drone.drone_buzzer(Note.E4, 300)  # Play E4 for 300ms

drone.land()

# Close connection to the drone
drone.close()